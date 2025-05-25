import streamlit as st
import pandas as pd
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.generate_mock_data import generate_mock_data
from utils.heatmap import generate_heatmap
from run_simulation import run_simulation

def main():
    st.title("Terrorism Threat Detection & Simulation Dashboard")
    
    # Sidebar controls
    st.sidebar.header("Controls")
    
    # File uploader
    uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=['csv'])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        df.to_csv('data/terrorism_mock.csv', index=False)
    else:
        if not os.path.exists('data/terrorism_mock.csv'):
            generate_mock_data()
    
    # Escalation threshold slider
    escalation_threshold = st.sidebar.slider(
        "Escalation Threshold",
        min_value=1,
        max_value=3,
        value=2,
        step=1,
        help="Only escalate if risk score is greater than or equal to this value"
    )
    
    # Run simulation button
    if st.sidebar.button("Run Simulation"):
        run_simulation()
        st.sidebar.success("Simulation completed!")
    
    # Main content
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Latest Simulation Results")
        if os.path.exists('logs/simulation_results.csv'):
            results_df = pd.read_csv('logs/simulation_results.csv')
            st.dataframe(results_df)
        else:
            st.info("No simulation results available. Run a simulation first.")
    
    with col2:
        st.header("Threat Heatmap")
        if os.path.exists('output/heatmap.html'):
            with open('output/heatmap.html', 'r', encoding='utf-8') as f:
                st.components.v1.html(f.read(), height=600)
        else:
            generate_heatmap()
            with open('output/heatmap.html', 'r', encoding='utf-8') as f:
                st.components.v1.html(f.read(), height=600)
    
    # Statistics section
    st.header("Statistics")
    if os.path.exists('logs/simulation_results.csv'):
        results_df = pd.read_csv('logs/simulation_results.csv')
        
        col3, col4, col5 = st.columns(3)
        
        with col3:
            st.metric("Total Incidents", len(results_df))
        
        with col4:
            high_risk_actions = len(results_df[results_df['action'].isin(['Alert', 'Neutralize'])])
            st.metric("High-Risk Actions Taken", high_risk_actions)
        
        with col5:
            avg_reward = results_df['reward'].mean()
            st.metric("Average Reward", f"{avg_reward:.2f}")

if __name__ == "__main__":
    main() 
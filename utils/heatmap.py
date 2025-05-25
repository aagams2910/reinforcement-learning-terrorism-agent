import pandas as pd
import plotly.express as px
import os

def generate_heatmap():
    # Load data
    df = pd.read_csv('data/terrorism_mock.csv')
    
    # Map threat levels to risk scores
    threat_scores = {'Low': 1, 'Medium': 2, 'High': 3}
    df['risk_score'] = df['threat_level'].map(threat_scores)
    
    # Create heatmap
    fig = px.density_mapbox(
        df,
        lat='lat',
        lon='lon',
        z='risk_score',
        radius=20,
        center=dict(lat=20.5937, lon=78.9629),  # Center of India
        zoom=4,  # Zoom level appropriate for India
        mapbox_style="carto-positron",
        title="India Terrorism Threat Heatmap",
        color_continuous_scale="RdYlBu_r"
    )
    
    # Update layout for better visualization
    fig.update_layout(
        margin={"r":0,"t":30,"l":0,"b":0},
        mapbox=dict(
            style="carto-positron",
            zoom=4,
            center=dict(lat=20.5937, lon=78.9629)
        )
    )
    
    # Create output directory if it doesn't exist
    os.makedirs('output', exist_ok=True)
    
    # Save the figure
    fig.write_html('output/heatmap.html')
    print("Heatmap generated and saved to output/heatmap.html")

if __name__ == "__main__":
    generate_heatmap() 
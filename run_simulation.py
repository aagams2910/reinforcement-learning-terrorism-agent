import os
import pandas as pd
from stable_baselines3 import PPO
from env.terrorism_env import TerrorismEnv
import logging
from datetime import datetime
import numpy as np

def run_simulation():
    # Setup logging
    os.makedirs('logs', exist_ok=True)
    logging.basicConfig(
        filename='logs/simulation.log',
        level=logging.INFO,
        format='%(message)s'
    )
    
    # Load the trained model
    model = PPO.load("models/ppo_terrorism")
    env = TerrorismEnv()
    
    # Load the data for reference
    data = pd.read_csv('data/terrorism_mock.csv')
    
    # Initialize simulation results
    results = []
    
    # Run simulation
    obs, _ = env.reset()
    done = False
    truncated = False
    
    while not (done or truncated):
        action, _ = model.predict(obs)
        # Convert action to integer, handling both scalar and array cases
        action_int = int(action.item() if isinstance(action, np.ndarray) else action)
        obs, reward, done, truncated, _ = env.step(action_int)
        
        # Get current data
        current_data = data.iloc[env.current_step - 1]
        
        # Map action to string
        action_map = {
            0: "Alert",
            1: "Ignore",
            2: "Escalate",
            3: "Neutralize"
        }
        
        # Record results
        result = {
            'id': current_data['id'],
            'date': current_data['date'],
            'location': current_data['location'],
            'action': action_map[action_int],
            'reward': reward
        }
        results.append(result)
        
        # Log the result
        logging.info(f"ID: {result['id']}, Date: {result['date']}, "
                    f"Location: {result['location']}, Action: {result['action']}, "
                    f"Reward: {result['reward']}")
    
    # Convert results to DataFrame and save
    results_df = pd.DataFrame(results)
    results_df.to_csv('logs/simulation_results.csv', index=False)
    print("Simulation completed! Results saved to logs/simulation_results.csv")

if __name__ == "__main__":
    run_simulation() 
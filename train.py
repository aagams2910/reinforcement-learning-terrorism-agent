import os
from stable_baselines3 import PPO
from env.terrorism_env import TerrorismEnv
from utils.generate_mock_data import generate_mock_data

def train_model():
    # Generate mock data if it doesn't exist
    if not os.path.exists('data/terrorism_mock.csv'):
        generate_mock_data()
    
    # Create and wrap the environment
    env = TerrorismEnv()
    
    # Initialize the model
    model = PPO(
        "MlpPolicy",
        env,
        verbose=1,
        learning_rate=0.0003,
        n_steps=2048,
        batch_size=64,
        n_epochs=10,
        gamma=0.99,
        gae_lambda=0.95,
        clip_range=0.2,
        tensorboard_log="./logs/"
    )
    
    # Train the model
    model.learn(total_timesteps=50000)
    
    # Create models directory if it doesn't exist
    os.makedirs('models', exist_ok=True)
    
    # Save the model
    model.save("models/ppo_terrorism")
    print("Training completed and model saved!")

if __name__ == "__main__":
    train_model() 
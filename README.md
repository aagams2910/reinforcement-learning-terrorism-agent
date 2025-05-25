# Preventive Agent: Terrorism Threat Detection & Simulation Engine

This project implements a Reinforcement Learning (RL) based system for simulating and detecting potential terrorism threats. It uses a custom Gym environment and Stable-Baselines3's PPO algorithm to train an agent that can make decisions about threat levels and appropriate responses.

## Project Structure

```
.
├── app/
│   └── streamlit_app.py      # Interactive dashboard
├── data/
│   └── terrorism_mock.csv    # Generated mock data
├── env/
│   └── terrorism_env.py      # Custom Gym environment
├── logs/                     # Simulation logs and results
├── models/                   # Trained RL models
├── output/                   # Generated visualizations
├── utils/
│   ├── generate_mock_data.py # Mock data generator
│   └── heatmap.py           # Heatmap visualization
├── train.py                 # Training script
├── run_simulation.py        # Simulation runner
└── requirements.txt         # Project dependencies
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/aagams2910/reinforcement-learning-terrorism-agent.git
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### 1. Generate Mock Data
The project includes a mock data generator that creates synthetic terrorism incident data:
```bash
python utils/generate_mock_data.py
```

### 2. Train the RL Model
Train the PPO agent on the mock data:
```bash
python train.py
```

### 3. Run Simulation
Run a simulation using the trained model:
```bash
python run_simulation.py
```

### 4. Launch Dashboard
Start the Streamlit dashboard:
```bash
streamlit run app/streamlit_app.py
```

## Features

- **Mock Data Generation**: Creates realistic synthetic data for training and testing
- **Custom Gym Environment**: Implements a custom environment for terrorism threat detection
- **PPO-based RL Agent**: Uses Stable-Baselines3's PPO implementation
- **Interactive Dashboard**: Streamlit-based dashboard for visualization and control
- **Heatmap Visualization**: Geographic visualization of threat levels
- **Simulation Logging**: Detailed logging of agent decisions and outcomes

## Environment Details

The custom Gym environment (`TerrorismEnv`) implements:
- Action space: 4 discrete actions (Alert, Ignore, Escalate, Neutralize)
- Observation space: Encoded features of incidents
- Reward structure:
  - +10 for correct Alert/Neutralize on High threat
  - -10 for ignoring High threat
  - -5 for false alarms
  - 0 for other cases

## Dashboard Features

The Streamlit dashboard provides:
- Upload custom CSV data
- Adjustable escalation threshold
- Real-time simulation results
- Interactive heatmap visualization
- Key performance metrics

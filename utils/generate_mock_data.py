import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_mock_data(n_samples=500):
    # Set random seed for reproducibility
    np.random.seed(42)
    random.seed(42)
    
    # Define possible values
    cities = [
        "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata",
        "Pune", "Ahmedabad", "Jaipur", "Lucknow", "Kanpur", "Nagpur",
        "Indore", "Thane", "Bhopal", "Visakhapatnam", "Patna", "Vadodara",
        "Ghaziabad", "Ludhiana", "Coimbatore", "Kochi", "Guwahati", "Chandigarh"
    ]
    
    incident_types = ["Bombing", "Shooting", "Hostage", "Cyberattack"]
    target_types = ["Government", "Civilians", "Infrastructure", "Military"]
    threat_levels = ["Low", "Medium", "High"]
    
    # Generate data
    data = {
        'id': range(1, n_samples + 1),
        'date': [
            (datetime(2020, 1, 1) + timedelta(days=random.randint(0, 1825))).strftime('%Y-%m-%d')
            for _ in range(n_samples)
        ],
        'location': random.choices(cities, k=n_samples),
        'incident_type': random.choices(incident_types, k=n_samples),
        'target_type': random.choices(target_types, k=n_samples),
        'threat_level': random.choices(threat_levels, k=n_samples)
    }
    
    # Generate coordinates for Indian cities
    city_coords = {
        "Mumbai": (19.0760, 72.8777),
        "Delhi": (28.6139, 77.2090),
        "Bangalore": (12.9716, 77.5946),
        "Hyderabad": (17.3850, 78.4867),
        "Chennai": (13.0827, 80.2707),
        "Kolkata": (22.5726, 88.3639),
        "Pune": (18.5204, 73.8567),
        "Ahmedabad": (23.0225, 72.5714),
        "Jaipur": (26.9124, 75.7873),
        "Lucknow": (26.8467, 80.9462),
        "Kanpur": (26.4499, 80.3319),
        "Nagpur": (21.1458, 79.0882),
        "Indore": (22.7196, 75.8577),
        "Thane": (19.2183, 72.9781),
        "Bhopal": (23.2599, 77.4126),
        "Visakhapatnam": (17.6868, 83.2185),
        "Patna": (25.5941, 85.1376),
        "Vadodara": (22.3072, 73.1812),
        "Ghaziabad": (28.6692, 77.4538),
        "Ludhiana": (30.9009, 75.8573),
        "Coimbatore": (11.0168, 76.9558),
        "Kochi": (9.9312, 76.2673),
        "Guwahati": (26.1445, 91.7362),
        "Chandigarh": (30.7333, 76.7794)
    }
    
    data['lat'] = [city_coords[city][0] + np.random.normal(0, 0.01) for city in data['location']]
    data['lon'] = [city_coords[city][1] + np.random.normal(0, 0.01) for city in data['location']]
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Save to CSV
    df.to_csv('data/terrorism_mock.csv', index=False)
    print(f"Generated mock data with {n_samples} samples")
    return df

if __name__ == "__main__":
    generate_mock_data() 
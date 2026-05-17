import pandas as pd
import os
from typing import Dict

def load_country_data(country: str, data_dir: str = "data") -> pd.DataFrame:
    """
    Load solar power data for a specific country.
    """
    filename = f"{country.lower()}.csv"
    filepath = os.path.join(data_dir, filename)
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Data file not found: {filepath}")
    
    df = pd.read_csv(filepath, parse_dates=['timestamp'])
    df = df.sort_values('timestamp').reset_index(drop=True)
    
    print(f"✅ Loaded {country} data: {df.shape[0]:,} rows, {df.shape[1]} columns")
    return df


def load_all_data(data_dir: str = "data") -> Dict[str, pd.DataFrame]:
    """Load data for all three countries."""
    countries = ['benin', 'sierraleone', 'togo']
    return {country.capitalize(): load_country_data(country, data_dir) for country in countries}
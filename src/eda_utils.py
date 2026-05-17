import pandas as pd
import numpy as np

def basic_info(df: pd.DataFrame, country_name: str):
    """Print basic information about the dataset."""
    print(f"\n{'='*20} {country_name} DATA INFO {'='*20}")
    print(f"Shape: {df.shape}")
    print(f"Date Range: {df['timestamp'].min()} to {df['timestamp'].max()}")
    print(f"Missing Values:\n{df.isnull().sum()}")
    print(f"Duplicate Rows: {df.duplicated().sum()}")


def summary_statistics(df: pd.DataFrame):
    """Return key summary statistics."""
    stats = df.describe()
    return stats


def check_missing_percentage(df: pd.DataFrame) -> pd.Series:
    """Calculate percentage of missing values per column."""
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    return missing_pct[missing_pct > 0].sort_values(ascending=False)


def detect_outliers_iqr(df: pd.DataFrame, column: str) -> tuple:
    """Detect outliers using IQR method."""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower) | (df[column] > upper)]
    return outliers, lower, upper
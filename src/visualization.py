import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd

sns.set_style("darkgrid")

def plot_time_series(df: pd.DataFrame, country: str, column: str = "GHI"):
    """Plot time series for a key column."""
    plt.figure(figsize=(14, 6))
    plt.plot(df['timestamp'], df[column], linewidth=1.5)
    plt.title(f'{country} - {column} Over Time')
    plt.xlabel('Date')
    plt.ylabel(column)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_power_vs_irradiance(df: pd.DataFrame, country: str):
    """Scatter plot between power and irradiance."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='GHI', y='Power', alpha=0.6)
    plt.title(f'{country} - Power Output vs Solar Irradiance')
    plt.xlabel('Global Horizontal Irradiance (GHI)')
    plt.ylabel('Power Output')
    plt.tight_layout()
    plt.show()


def correlation_heatmap(df: pd.DataFrame, country: str):
    """Plot correlation heatmap."""
    numeric_df = df.select_dtypes(include=np.number)
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', center=0)
    plt.title(f'{country} - Correlation Heatmap')
    plt.tight_layout()
    plt.show()


def compare_countries_hist(data_dict: dict, column: str = "GHI"):
    """Compare distribution across countries."""
    plt.figure(figsize=(12, 6))
    for country, df in data_dict.items():
        sns.kdeplot(df[column], label=country, fill=True, alpha=0.4)
    plt.title(f'Distribution of {column} Across Countries')
    plt.xlabel(column)
    plt.ylabel('Density')
    plt.legend()
    plt.show()
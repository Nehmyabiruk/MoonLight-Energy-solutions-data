from src.data_loader import load_all_data
from src.eda_utils import basic_info, check_missing_percentage
from src.visualization import plot_time_series, compare_countries_hist

if __name__ == "__main__":
    print("🌙 MoonLight Energy Solutions - Starting Analysis...\n")
    
    data = load_all_data()
    
    for country, df in data.items():
        basic_info(df, country) bdtsvkhudc
    
    compare_countries_hist(data, column="GHI")
    print("\n✅ Analysis completed successfully!")

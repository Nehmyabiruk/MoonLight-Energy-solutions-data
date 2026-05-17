# 🌙 MoonLight Energy Solutions - Solar Data Analysis

**Week 0 | 10 Academy Data Analytics Project**



### 📋 Project Overview

Comprehensive **Exploratory Data Analysis (EDA)** on solar power generation and weather data from **Benin, Sierra Leone, and Togo**. 

This project analyzes solar irradiance, power output, and weather patterns to help MoonLight Energy Solutions optimize performance, identify maintenance needs, and support data-driven expansion across West Africa.

---

### 🎯 Objectives

- Perform in-depth EDA on solar datasets from three countries
- Compare energy performance across Benin, Sierra Leone, and Togo
- Ensure clean, reproducible, and professional project structure
- Build reusable code modules for future analysis

---

### 📂 Project Structure

```bash
MoonLight-Energy-solutions-data/
├── data/                      # Raw and cleaned datasets
│   ├── benin.csv
│   ├── sierraleone.csv
│   ├── togo.csv
│   └── *_clean.csv
├── notebooks/                 # Main analysis notebooks
│   └── moon_light_professional_eda.ipynb
├── src/                       # Reusable Python modules
│   ├── __init__.py
│   ├── data_loader.py
│   ├── eda_utils.py
│   └── visualization.py
├── plots/                     # Generated visualizations
├── requirements.txt
├── main.py
├── .gitignore
└── README.md

🛠️ Technologies Used

Python 3.10+
pandas, NumPy
Matplotlib, Seaborn, Plotly
Jupyter Notebook
SciPy


🚀 Quick Start
1. Clone the Repository
Bashgit clone https://github.com/Nehmyabiruk/MoonLight-Energy-solutions-data.git
cd MoonLight-Energy-solutions-data
2. Create Virtual Environment (Recommended)
Bashpython -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
# source venv/bin/activate
3. Install Dependencies
Bashpip install -r requirements.txt
4. Run the Analysis
Option A: Using VS Code (Recommended)

Open the project folder in VS Code
Open notebooks/moon_light_professional_eda.ipynb
Select Python kernel and run the cells

Option B: Using Terminal
Bashjupyter notebook

📊 Key Analysis Includes

Data loading and quality assessment
Time series visualization of solar irradiance and power output
Correlation analysis between weather and power generation
Cross-country comparison
Data cleaning and outlier handling
Interactive Plotly visualizations


📈 Future Enhancements

Streamlit / Power BI interactive dashboard
Predictive modeling for power output forecasting
Automated daily reporting system
Anomaly detection for faulty solar panels


Made with ❤️ by Nehmyabiruk
10 Academy Data Science Program - Week 0

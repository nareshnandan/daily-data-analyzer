import pandas as pd
import matplotlib.pyplot as plt

# Load CSV Data
def load_data(filepath):
    try:
        data = pd.read_csv(filepath)
        print("✅ Data loaded successfully.")
        print(data.head())
        return data
    except Exception as e:
        print("Error loading file:", e)
        return None

# Summarize the data
def summarize_data(data):
    print("\n Data Summary:")
    print("-" * 40)
    print(f"Shape of data: {data.shape}")
    
    print("\n Column names and types:")
    print(data.dtypes)

    print("\n Missing values in each column:")
    print(data.isnull().sum())

    print("\n Statistical Summary:")
    print(data.describe())

# Plot salary bar chart
def plot_salary_chart(data):
    plt.figure(figsize=(8, 5))
    plt.bar(data["Name"], data["Salary"], color="skyblue")
    plt.title("Employee Salary Chart")
    plt.xlabel("Name")
    plt.ylabel("Salary")
    plt.tight_layout()
    
    # Save chart to 'plots' folder
    plt.savefig("plots/salary_chart.png")
    plt.show()
    print("Chart saved to plots/salary_chart.png")

# ---- MAIN ----
df = load_data("data/sample.csv")
if df is not None:
    summarize_data(df)
    plot_salary_chart(df)

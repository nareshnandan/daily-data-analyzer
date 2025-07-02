import pandas as pd
import matplotlib.pyplot as plt

# Load CSV Data
def load_data(filepath):
    if not filepath.endswith(".csv"):
        print("Error: Only CSV files are supported.")
        return None

    try:
        data = pd.read_csv(filepath)
        print("Data loaded successfully.")
        print(data.head())
        return data
    except Exception as e:
        print("Error loading file:", e)
        return None

    
def handle_missing_data(data):
    print("\n Handling Missing Data")
    print("-" * 40)
    print("Before cleaning:")
    print(data.isnull().sum())

    # Fill missing Age with average Age
    if "Age" in data.columns:
        mean_age = data["Age"].mean()
        data["Age"].fillna(mean_age, inplace=True)

    # Drop rows where Salary is missing
    data.dropna(subset=["Salary"], inplace=True)

    print("\n After cleaning:")
    print(data.isnull().sum())
    return data

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

def show_top_earners(data, count=3):
    print(f"\n Top {count} Earners:")
    top_earners = data.sort_values(by="Salary", ascending=False).head(count)
    print(top_earners[["Name", "Salary"]])
    
    # Save to CSV
    top_earners.to_csv("data/top_earners.csv", index=False)
    print("✅ Top earners saved to data/top_earners.csv")



# ---- MAIN ----
df = load_data("data/sample.csv")
if df is not None:
    summarize_data(df)
    df = handle_missing_data(df)
    plot_salary_chart(df)
    show_top_earners(df)


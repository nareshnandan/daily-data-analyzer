import pandas as pd

def load_data(filepath):
    try:
        data = pd.read_csv(filepath)
        print("Data loaded successfully.")
        print(data.head())
        return data
    except Exception as e:
        print("Error loading file:", e)
        return None

def summarize_data(data):
    print("\n🔍 Data Summary:")
    print("-" * 40)
    print(f"Shape of data: {data.shape}")
    print("\nColumn names and types:")
    print(data.dtypes)

    print("\nMissing values in each column:")
    print(data.isnull().sum())

    print("\n📊 Statistical Summary:")
    print(data.describe())

# ---- TEST ----
df = load_data("data/sample.csv")
if df is not None:
    summarize_data(df)

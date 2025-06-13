import pandas as pd

def load_data(filepath):
    try:
        data = pd.read_csv(filepath)
        print("Data loaded successfully.")
        print(data.head())
    except Exception as e:
        print("Error loading file:", e)

# Example usage
load_data("data/sample.csv")

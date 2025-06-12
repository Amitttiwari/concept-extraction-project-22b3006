import pandas as pd
import os

def read_csv(subject):
    file_path = os.path.join("resources", f"{subject}.csv")
    try:
        df = pd.read_csv(file_path)
        # Normalize column names
        df.columns = [col.strip().lower().replace('.', '') for col in df.columns]
        return df
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

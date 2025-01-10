
import pandas as pd

# Function to clean a dataset
def clean_data(file_path):
    # Load dataset
    df = pd.read_csv(file_path)
    
    # Drop duplicate rows
    df = df.drop_duplicates()
    
    # Fill missing values with default values
    df = df.fillna({'Column1': 'Default', 'Column2': 0})
    
    # Standardize column names
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    
    return df

# Example usage
if __name__ == "__main__":
    cleaned_data = clean_data("sample_data.csv")
    print(cleaned_data.head())

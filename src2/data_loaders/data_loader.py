import os
import pandas as pd
from tqdm import tqdm  # Import tqdm for progress bar

import sys
sys.path.append(r"C:\Users\paxec\OneDrive\Documents\GitHub\Upskiller\statscompute\src2\data_loader")

from feature_engineering import extract_features

def load_data_from_directory(directory):
    """Load and return data from all text files in the specified directory as a pandas DataFrame."""
    all_data = []
    filepaths = []  # Store file paths to extract filenames

    files = [f for f in os.listdir(directory) if f.endswith('.txt')]  # List of .txt files
    for filename in tqdm(files, desc="Processing files"):  # tqdm wraps the iterable
        filepath = os.path.join(directory, filename)
        filepaths.append(filepath)  # Store full file path

        with open(filepath, 'r') as file:
            file_data = file.read()
            processed_data = process_file_data(file_data)
            if processed_data:
                all_data.append(processed_data)

    return pd.DataFrame(all_data), filepaths  # Return DataFrame + filepaths

def process_file_data(file_data):
    """Process and return structured data from the file content."""
    structured_data = {}
    for line in file_data.splitlines():
        if ':' in line:
            key, value = line.split(':', 1)  # Split only on the first occurrence
            try:
                structured_data[key.strip()] = float(value.strip())
            except ValueError:
                pass  # Optionally handle or log the error silently if needed
        else:
            pass  # Malformed lines are silently ignored
    return structured_data

if __name__ == '__main__':
    directory_path = r'G:\Shared drives\01_Project_Belysningsstiftelse\02_Development\Datasets\Dataset\others\features'
    
    # Load data + filepaths
    data_df, filepaths = load_data_from_directory(directory_path)

    # Apply Feature Extraction (Pass both DataFrame & Filepaths)
    data_df = extract_features(data_df, filepaths)

    output_path = r'G:\Shared drives\01_Project_Belysningsstiftelse\02_Development\stats\output_data.csv'
    data_df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")

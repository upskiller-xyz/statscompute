import os
import pandas as pd
import matplotlib.pyplot as plt

# Path to the processed dataset
csv_path = r'G:\Shared drives\01_Project_Belysningsstiftelse\02_Development\stats\output_data.csv'
output_dir = r'G:\Shared drives\01_Project_Belysningsstiftelse\02_Development\stats\histograms'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Check if file exists before proceeding
if not os.path.exists(csv_path):
    print(f"Error: File not found at {csv_path}")
else:
    # Load dataset
    df = pd.read_csv(csv_path)

    # Identify boolean columns (columns that contain only 0 and 1)
    boolean_columns = [col for col in df.columns if df[col].dropna().isin([0, 1]).all()]

    # Identify numeric columns (excluding 'seed')
    numeric_columns = [col for col in df.columns if col not in boolean_columns + ['seed']]

    # Create histograms for numeric columns with 50 bins
    for col in numeric_columns:
        plt.figure(figsize=(8, 5))
        df[col].hist(bins=50)  # 50 bins for numeric columns
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.grid(False)
        safe_col_name = ''.join(c if c.isalnum() or c in (' ', '_') else '_' for c in col)  # Sanitize filename
        plt.savefig(os.path.join(output_dir, f"{safe_col_name}_histogram.png"))  # Save histogram as image
        plt.close()

    # Create histograms for boolean columns with only 2 bins
    for col in boolean_columns:
        plt.figure(figsize=(8, 5))
        df[col].hist(bins=2)  # 2 bins for boolean columns
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.xticks([0, 1])  # Ensure only 0 and 1 are displayed
        plt.grid(False)
        safe_col_name = ''.join(c if c.isalnum() or c in (' ', '_') else '_' for c in col)  # Sanitize filename
        plt.savefig(os.path.join(output_dir, f"{safe_col_name}_histogram.png"))  # Save histogram as image
        plt.close()

    print(f"Histograms saved in: {output_dir}")

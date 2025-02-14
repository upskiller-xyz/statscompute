import pandas as pd
import numpy as np
import os

def extract_features(df, filepaths):
    """Generate new features for each individual window, its corresponding wall, and room.
       Skips rows with missing values and those where avgeDF, medianDF, and sDA300/50 are all zero.
    """
    
    # Extract filenames without path and extension as 'seed' column
    filenames = [os.path.splitext(os.path.basename(path))[0] for path in filepaths]
    df.insert(0, 'seed', filenames)
    
    # Calculate the window area
    if 'windowDimVertical' in df.columns and 'windowDimHorizontal' in df.columns:
        df['WindowArea'] = df['windowDimVertical'] * df['windowDimHorizontal']
        df['WindowArea'] = df['WindowArea'].round(2)  # ✅ Round to 2 decimal places
    
    # Calculate the wall area where the window is placed
    if 'windowWallLength' in df.columns and 'roomHeight' in df.columns:
        df['WallArea'] = df['windowWallLength'] * df['roomHeight']
        df['WallArea'] = df['WallArea'].round(2)  # ✅ Round to 2 decimal places
    
    # Calculate Window-to-Wall Ratio (WWR)
    if 'WindowArea' in df.columns and 'WallArea' in df.columns:
        df['WWR'] = df['WindowArea'] / df['WallArea']
        df['WWR'].replace([np.inf, -np.inf], np.nan, inplace=True)  # Avoid division by zero
        df['WWR'] = df['WWR'].round(2)  # ✅ Round WWR to 2 decimal places

    # Calculate Window-to-Floor Ratio (WFR)
    if 'WindowArea' in df.columns and 'RoomArea' in df.columns:
        df['WFR'] = df['WindowArea'] / df['RoomArea']
        df['WFR'].replace([np.inf, -np.inf], np.nan, inplace=True)  # Avoid division by zero
        df['WFR'] = df['WFR'].round(2)  # ✅ Round WFR to 2 decimal places

    # Round sDA300/50 to 2 decimal places
    if 'sDA300/50' in df.columns:
        df['sDA300/50'] = df['sDA300/50'].round(2)

    # Count rows before filtering
    total_rows_before = len(df)

    # Remove rows with missing values
    df.dropna(inplace=True)

    # Remove rows where avgeDF, medianDF, and sDA300/50 are all zero
    if {'avgeDF', 'medianDF', 'sDA300/50'}.issubset(df.columns):
        df = df[~((df['avgeDF'] == 0) & (df['medianDF'] == 0) & (df['sDA300/50'] == 0))]

    # Count rows after filtering
    total_rows_after = len(df)
    skipped_rows = total_rows_before - total_rows_after

    # Print number of skipped rows
    print(f"Skipped {skipped_rows} data points due to missing values or invalid conditions.")

    # Ensure WWR, WFR, WindowArea, and WallArea are placed right after "heightSillOverFloor"
    target_position = df.columns.get_loc("heightSillOverFloor") + 1  # Find index of heightSillOverFloor and shift by 1
    cols = list(df.columns)
    
    # Move WWR, WFR, WindowArea, and WallArea to the desired position
    for col in ["WWR", "WFR", "WindowArea", "WallArea"]:
        if col in cols:
            cols.remove(col)  # Remove from current position
            cols.insert(target_position, col)  # Insert at correct position
            target_position += 1  # Shift the index for correct ordering

    # Sort DataFrame by 'seed' column
    df = df.sort_values(by='seed').reset_index(drop=True)
    
    return df[cols]  # Return DataFrame with reordered columns

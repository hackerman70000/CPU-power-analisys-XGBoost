import os
import pandas as pd
import glob
import numpy as np


def prepare_dataset(input_folder, output_folder):
    input_path = os.path.join("resources", input_folder)
    output_path = os.path.join("resources", output_folder)

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    files = os.listdir(input_path)

    # Data cleansing
    for i, file_name in enumerate(files):
        if file_name.endswith(".csv"):
            df = pd.read_csv(os.path.join(input_path, file_name))
            df["Encrypting"] = (df['D0'] == 1) & (df['D1'] == 0)
            df = df.drop(columns=['D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7'])
            new_file_name = f"dataset{i + 1}.csv"
            calculate_averages(df)
            df = df.dropna()
            df.to_csv(os.path.join(output_path, new_file_name), index=False)
    print("Data enrichment has been completed.")
    print("Data processing has been completed.")


def calculate_averages(df):
    window_sizes = [3, 5, 7, 10, 15, 20, 50, 100]

    # Compute moving averages for each window size
    for window_size in window_sizes:
        col_name = f'MA_{window_size}'
        df[col_name] = df['Current(uA)'].rolling(window=window_size).mean().round(3)

        # Weighted Moving Average (WMA)
        wma_col_name = f'WMA_{window_size}'
        weights = list(range(1, window_size + 1))
        df[wma_col_name] = df['Current(uA)'].rolling(window=window_size).apply(
            lambda x: np.dot(x, weights) / sum(weights), raw=True).round(3)

        # Exponential Moving Average (EMA)
        ema_col_name = f'EMA_{window_size}'
        df[ema_col_name] = df['Current(uA)'].ewm(span=window_size, adjust=False).mean().round(3)


def concatenate_datasets(input_folder, output_folder):
    input_path = os.path.join("resources", input_folder)
    output_path = os.path.join("resources", output_folder)

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    files = glob.glob(os.path.join(input_path, "*.csv"))

    dfs = []

    for file in files:
        df = pd.read_csv(file)
        dfs.append(df)

    data = pd.concat(dfs, ignore_index=True)
    data.dropna(inplace=True)
    data.to_csv(os.path.join(output_path, "concatenated_dataset.csv"), index=False)
    print("Data concatenation has been completed.")


if __name__ == "__main__":
    prepare_dataset("raw_data", "prepared_data")
    concatenate_datasets("prepared_data", "concatenated_data")
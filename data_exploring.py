import matplotlib.pyplot as plt
import pandas as pd


def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("Error: File not found. Please make sure the file exists.")
        return None


def plot_histograms(data):
    data['Color'] = data['Encrypting'].map({True: 'blue', False: 'green'})

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.hist(data[data['Encrypting']]['Current(uA)'], bins=50, color='blue', edgecolor='blue', alpha=0.7)
    plt.title('CPU is performing encryption')
    plt.xlabel('Current(uA)')
    plt.ylabel('Frequency')
    plt.xlim(200000, 250000)
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.hist(data[~data['Encrypting']]['Current(uA)'], bins=500, color='green', edgecolor='green', alpha=0.7)
    plt.title('CPU is not performing encryption')
    plt.xlabel('Current(uA)')
    plt.ylabel('Frequency')
    plt.xlim(200000, 250000)
    plt.legend()

    plt.tight_layout()
    plt.show()


def plot_current_over_time(data):
    plt.figure(figsize=(12, 6))
    plt.scatter(data['Timestamp(ms)'], data['Current(uA)'], color=data['Color'], alpha=0.7, s=1)
    plt.title('Current over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('Current(uA)')
    plt.legend()
    plt.show()


def plot_current_ma_ema(data):
    plt.figure(figsize=(10, 6))

    plt.scatter(data['Timestamp(ms)'], data['Current(uA)'], label='Current', s=1)

    plt.plot(data['Timestamp(ms)'], data['MA_10'], label='MA(10)', color='turquoise')

    plt.plot(data['Timestamp(ms)'], data['EMA_100'], label='EMA(100)', color='palegreen')

    plt.xlabel('Timestamp (ms)')
    plt.ylabel('Current (uA)')
    plt.title('Current Over Time with MA(10) and EMA(100)')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    data = load_data("resources/prepared_data/sample.csv")
    if data is not None:
        plot_histograms(data)
        plot_current_over_time(data)
        plot_current_ma_ema(data)

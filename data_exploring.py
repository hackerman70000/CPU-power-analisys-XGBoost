import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("resources/prepared_data/sample.csv")

data['Color'] = data['Encrypting'].map({True: 'blue', False: 'green'})

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(data[data['Encrypting']]['Current(uA)'], bins=50, color='blue', edgecolor='black', alpha=0.7)
plt.title('CPU is performing encryption')
plt.xlabel('Current(uA)')
plt.ylabel('Frequency')
plt.xlim(200000, 250000)

plt.subplot(1, 2, 2)
plt.hist(data[~data['Encrypting']]['Current(uA)'], bins=500, color='green', edgecolor='black', alpha=0.7)
plt.title('CPU is not performing encryption')
plt.xlabel('Current(uA)')
plt.ylabel('Frequency')
plt.xlim(200000, 250000)

print(data['Current(uA)'].describe())
print(data.describe())

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.scatter(data['Timestamp(ms)'], data['Current(uA)'], color=data['Color'], alpha=0.7)
plt.title('Current over Time')
plt.xlabel('Timestamp')
plt.ylabel('Current(uA)')
plt.show()

import os
import matplotlib.pyplot as plt
import pandas as pd
import xgboost as xgb
from sklearn.metrics import precision_score, accuracy_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import plot_tree
from imblearn.under_sampling import RandomUnderSampler

file_path = "resources/concatenated_data/concatenated_dataset.csv"

if not os.path.exists(file_path):
    raise FileNotFoundError(f"File '{file_path}' not found. Please make sure the file exists.")

try:
    data = pd.read_csv(file_path)
except Exception as e:
    print("Error occurred while reading the CSV file:", e)

window_sizes = [3, 5, 7, 10, 15, 20, 50, 100]

features = data[
    ['Timestamp(ms)', 'Current(uA)'] + [f'MA_{window_size}' for window_size in window_sizes] +
    [f'WMA_{window_size}' for window_size in window_sizes] + [f'EMA_{window_size}' for window_size in window_sizes]]

label = data["Encrypting"]

label_encoder = LabelEncoder()
labels = label_encoder.fit_transform(label)

rus = RandomUnderSampler()
features_resampled, labels_resampled = rus.fit_resample(features, labels)

X_train, X_test, y_train, y_test = train_test_split(features_resampled, labels_resampled, test_size=0.1)
model = xgb.XGBClassifier()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

precision = precision_score(y_test, predictions, zero_division=1)
print("Precision score: %.2f%%" % (precision * 100.0))

recall = recall_score(y_test, predictions, zero_division=1)
print("Recall score: %.2f%%" % (recall * 100.0))

accuracy = accuracy_score(y_test, predictions)
print("Accuracy score: %.2f%%" % (accuracy * 100.0))

try:
    plot_tree(model)
    plt.show()
except Exception as e:
    print("Error occurred while plotting tree:", e)

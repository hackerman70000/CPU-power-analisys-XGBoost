import matplotlib.pyplot as plt
import pandas as pd
import xgboost as xgb
from sklearn.metrics import precision_score, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import plot_tree

data = pd.read_csv("resources/concatenated_data/concatenated_dataset.csv")

window_sizes = [3, 5, 7, 10, 15, 20, 50, 100]

features = data[
    ['Timestamp(ms)', 'Current(uA)'] + [f'MA_{window_size}' for window_size in window_sizes] + [
        f'WMA_{window_size}' for window_size in window_sizes] + [f'EMA_{window_size}' for window_size in window_sizes]]

label = data["Encrypting"]
label_encoder = LabelEncoder()
labels = label_encoder.fit_transform(label)

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.1)

class_weights = {0: 200, 1: 1}
scale_pos_weight = sum(class_weights.values()) / sum(class_weights.keys())

model = xgb.XGBClassifier(scale_pos_weight=scale_pos_weight)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

precision = precision_score(y_test, predictions, zero_division=1)
print("Precision score: %.2f%%" % (precision * 100.0))

accuracy = accuracy_score(y_test, predictions)
print("Accuracy score: %.2f%%" % (accuracy * 100.0))

plot_tree(model)
plt.show()

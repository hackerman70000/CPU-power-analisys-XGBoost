# CPU Power Usage Analysis [XGBoost]

### Description

This project focuses on measuring CPU power consumption to determine encryption execution time. The aim is to understand
the duration of processor activity during encryption tasks using XGBoost.

### Motivation

This project is motivated by the paper "Lend Me Your Ear: Passive Remote Physical Side Channels on PCs" [1].
Power consumption of the CPU can be a vulnerability for side-channel attacks.
More complex analysis would allow us to infer what is happening on the victim's computer.

### Data

Data was collected by my colleague JB from the CPU Cora Z7 using the Nordic Power Profiling Kit II.

- The data is very noisy and required smoothing out, so I added variations of Moving Averages.

![Figure_3.png](images%2FFigure_3.png)

- The encryption time is much less frequent than non-encryption time. To deal with the imbalanced dataset, I used
  undersampling of the dominant class.

![Figure_2.png](images%2FFigure_2.png)

### Code

- data_preprocessing.py - contains the code for data preprocessing:
    - adding moving averages
    - concatenating data
- data_exploring.py - contains the code for data exploration and visualization
- model.py - contains the code for model training and evaluation

### Model

- XGBoost was used to train the model.
- Parameters found using GridSearchCV wasn't the best, so I used the default parameters.

### Results

Results are very promising:

- Precision score > 0.99
- Recall score > 0.99
- Accuracy score > 0.99

### References

[1] “Lend MeYour Ear: Passive Remote Physical Side Channels on PCs” Daniel Genkin; Noam Nissan; Roei Schuster; Eran
Tromer
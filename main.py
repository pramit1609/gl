# Import necessary libraries
import os
import json
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import GridSearchCV, train_test_split
from joblib import dump
import sys
import pandas as pd

# Function to load data from CSV files in a specified directory
def get_data(base_dir):
     # List CSV files in the directory
    data_file_names = [x for x in os.listdir(base_dir) if x.endswith('.csv')]
    data = {}
    for name in data_file_names:
        path_file = os.path.join(base_dir, name)
        data[name] = pd.read_csv("C:\Users\pramit\PycharmProjects\pythonProject4\Model\Iris.csv")
    return data

# Function to split data into training and testing sets
def split_data(data, test_size=0.2, random_state=42):
    df = data['iris.csv']
    X = df.drop('variety', axis=1)
    y = df['variety']
# Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    return {'X_train': X_train, 'X_test': X_test, 'y_train': y_train, 'y_test': y_test}

# Function to train a Logistic Regression model using grid search for hyperparameter tuning
def train_model(X_train, y_train):
    clf = LogisticRegression(max_iter=1000, random_state=200)
    mod = GridSearchCV(clf, param_grid={'C': [0.001, 0.01, 0.1, 1, 10, 100]})
    mod.fit(X_train, y_train)
    m = mod.best_estimator_
    return m

# Function to save the trained model to a file
def save_model(m):
    dump(m, '../Model/irispred.joblib')
    print("Model saved")

# Main script execution
if __name__ == "__main__":
    base_dir = r'C:\Users\pramit\PycharmProjects\pythonProject3\Model\Iris.csv'
    data = get_data(base_dir)

    split_data = split_data(data['iris.csv'])

    m = train_model(split_data['X_train'], split_data['y_train'])
    metrics = create_metrics(split_data['X_test'], split_data['y_test'], m)
    save_model(m)
    save_metrics(metrics)




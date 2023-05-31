#!/usr/bin/env python3

#original code from Kaggle notebook: https://www.kaggle.com/code/juanhdzma/survivability-predictor-ann-lr-svm-0-772 
#code has been modified to be used in Brane Context


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, jaccard_score
from sklearn.linear_model import LogisticRegression
import pickle
import datetime

def train_LR_model(dataset_path: str) -> str:
    # Load the dataset
#    dataset_path = f"{dataset_path}/dataset.csv"
    data = pd.read_csv(dataset_path)

    # Separate predictors and target
    predictors = data.drop(["Survived", "PassengerId"], axis=1)  # Drop 'Survived' and 'PassengerId'
    target = data["Survived"]

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(predictors, target, test_size=0.2)

    # Train the Logistic Regression model
    lr = LogisticRegression(solver='liblinear')
    lr.fit(X_train, y_train)

    # Save the trained model as a pickle file
    timestamp = datetime.datetime.utcnow()
    with open("/result/LR_trained_model.pickle", "wb") as f:
        pickle.dump(lr, f)

    return "/result/LR_trained_model.pickle"


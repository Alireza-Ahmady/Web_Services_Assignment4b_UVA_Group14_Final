#!/usr/bin/python3

#original code from Kaggle notebook: https://www.kaggle.com/code/juanhdzma/survivability-predictor-ann-lr-svm-0-772 
#code has been modified to be used in Brane Context

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def create_submission(clean_test_path: str, model_path: str) -> str:

    # Load the test dataset
    test_data = pd.read_csv(clean_test_path)

    # Extract ids
    ids = test_data['PassengerId']
    # Drop 'PassengerId' from the test set before making predictions
    test_data.drop(columns=['PassengerId'], inplace=True)

    # Load the trained model from the pickle file
    with open(model_path, 'rb') as file:
        trained_model = pickle.load(file)


    # Apply the trained model to the test dataset for prediction
    predictions = trained_model.predict(test_data)

    print("Predictions:", predictions)
    
    # Fusion the IDs with predictions, and then, generate a csv with that information
    result = list(zip(ids, predictions))
    result = pd.DataFrame(result, columns=['PassengerId', 'Survived'])
    filename = f"/result/submission.csv"
    result.to_csv(filename, index=False)
    
    return filename

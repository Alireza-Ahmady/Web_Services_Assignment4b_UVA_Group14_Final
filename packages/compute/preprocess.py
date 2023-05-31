#!/usr/bin/python3

#original code from Kaggle notebook: https://www.kaggle.com/code/juanhdzma/survivability-predictor-ann-lr-svm-0-772 
#code has been modified to be used in Brane Context

from sklearn.preprocessing import StandardScaler
from sklearn.impute import KNNImputer
import pandas as pd


def clean_data(dataset_path: str) -> str:
    # Read the dataset from the given path
    dataset_path = f"{dataset_path}/dataset.csv"
    dataset = pd.read_csv(dataset_path)
    
    # Make a deep copy of the dataset
    clean_dataset = dataset.copy()
    
    # Drop unused columns
    clean_dataset.drop(columns=['Name', 'Ticket'], axis=1, inplace=True, errors='ignore')
    
    # Categorical Values
    
    # Categorize the 'Cabin' attribute
    clean_dataset['Cabin'] = clean_dataset['Cabin'].notnull().astype(int)
    
    # Categorize the 'Sex' attribute
    clean_dataset['Sex'] = clean_dataset['Sex'].map({'male': 0, 'female': 1})
    
    # Delete the rows with null 'Embarked' values
    clean_dataset.dropna(subset=['Embarked'], inplace=True)
    
    # One-hot encode the 'Embarked' attribute
    one_hot_encoded = pd.get_dummies(clean_dataset['Embarked'], prefix='Embarked')
    clean_dataset = pd.concat([clean_dataset, one_hot_encoded], axis=1)
    clean_dataset.drop('Embarked', axis=1, inplace=True)
    
    
    #perform posterior imputation using KNNImputer on the 'Age' attribute
    imputer = KNNImputer(n_neighbors=5)
    clean_dataset['Age'] = imputer.fit_transform(clean_dataset[['Age']])
    clean_dataset['Age'] = clean_dataset['Age'].astype(int)
    
    #Apply MinMax scaling to 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare' attributes
    columns_to_normalize = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
    subset = clean_dataset[columns_to_normalize]
    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(subset)
    normalized_df = pd.DataFrame(normalized_data, columns=columns_to_normalize)
    clean_dataset[columns_to_normalize] = normalized_df
    
    #save the cleaned dataset as a new CSV file
    new_path = "/result/cleaned_dataset.csv"
    clean_dataset.to_csv(new_path)
    
    return new_path



def remove_null_values(dataset_path: str) -> str:
    #read the dataset from the input CSV file
    dataset_path = f"{dataset_path}/cleaned_dataset.csv"
    dataset = pd.read_csv(dataset_path)
    
    # drop rows with any remaining null values
    dataset.dropna(how='any', inplace=True)
    
    #save the cleaned dataset as a new CSV file
    new_path = "/result/cleaned_dataset.csv"
    dataset.to_csv(new_path, index=False)
    
    return new_path



#!/usr/bin/env python3

#original code from Kaggle notebook: https://www.kaggle.com/code/juanhdzma/survivability-predictor-ann-lr-svm-0-772 
#code has been modified to be used in Brane Context

import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import io
from typing import Counter

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  
import os


def load_dataset(data_path, merge_path=None):
    dataset = pd.read_csv(data_path)
    if merge_path and 'train' not in data_path:
        merge_dataset = pd.read_csv(merge_path)
        dataset = pd.merge(dataset, merge_dataset, on='PassengerId')
    return dataset
    

def plot_categorical_attributes(data_path, merge_path=None, store_file=True):
    dataset_name = os.path.splitext(os.path.basename(data_path))[0]
    if merge_path:
        dataset_name += '_' + os.path.splitext(os.path.basename(merge_path))[0]
    
    dataset = load_dataset(data_path, merge_path)

    categorical_attributes = ['Pclass', 'Sex', 'Embarked']
    fig, axes = plt.subplots(nrows=len(categorical_attributes), ncols=1, figsize=(8, len(categorical_attributes)*5))

    for i, attribute in enumerate(categorical_attributes):
        ax = axes[i]
        grouped_data = dataset.groupby([attribute, 'Survived']).size().unstack()
        percentage_data = grouped_data.div(grouped_data.sum(axis=1), axis=0) * 100
        percentage_data.plot(kind='bar', stacked=False, ax=ax)
        ax.set_xlabel(attribute)
        ax.set_ylabel('Percentage')
        ax.set_title(f'Percentages of Passengers that Survived by {attribute} ({dataset_name})')
        ax.legend(title='Survived')

        for container in ax.containers:
            ax.bar_label(container, label_type='center', fmt='%.1f%%', padding=0.4)

    plt.tight_layout()

    if store_file:
        filename = f"/result/categorical_attributes_{dataset_name}.png"
        plt.savefig(filename, dpi=300, bbox_inches="tight")

    buf = BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    base64_string = base64.b64encode(buf.getbuffer()).decode("ascii")

    return f'<img src="data:image/png;base64,{base64_string}" />'


def plot_numeric_attributes(data_path, merge_path=None, store_file=True):
    dataset_name = os.path.splitext(os.path.basename(data_path))[0]
    if merge_path:
        dataset_name += '_' + os.path.splitext(os.path.basename(merge_path))[0]
    
    dataset = load_dataset(data_path, merge_path)
    numeric_attributes = ['Age', 'SibSp', 'Parch', 'Fare']
    fig, axes = plt.subplots(nrows=len(numeric_attributes), figsize=(8, len(numeric_attributes)*4))

    for i, attribute in enumerate(numeric_attributes):
        ax = axes[i]
        sns.violinplot(data=dataset, x='Survived', y=attribute, ax=ax)
        ax.set_xlabel('Survived')
        ax.set_ylabel(attribute)
        ax.set_title(f'{attribute} by Survived ({dataset_name})')

    plt.tight_layout()

    if store_file:
        filename = f"/result/numeric_attributes_{dataset_name}.png"
        plt.savefig(filename, dpi=300, bbox_inches="tight")

    buf = BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    base64_string = base64.b64encode(buf.getbuffer()).decode("ascii")

    return f'<img src="data:image/png;base64,{base64_string}" />'


def plot_correlation_matrix(data_path, merge_path=None, store_file=True):
    dataset_name = os.path.splitext(os.path.basename(data_path))[0]
    if merge_path:
        dataset_name += '_' + os.path.splitext(os.path.basename(merge_path))[0]
    
    dataset = load_dataset(data_path, merge_path)
    correlation_matrix = dataset.corr(numeric_only=True)

    fig, ax = plt.subplots()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.tight_layout()

    if store_file:
        filename = f"/result/correlation_matrix_{dataset_name}.png"
        plt.savefig(filename, dpi=300, bbox_inches="tight")

    buf = BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    base64_string = base64.b64encode(buf.getbuffer()).decode("ascii")

    return f'<img src="data:image/png;base64,{base64_string}" />'


def plot_survival_percentage(data_path, store_file=True):
    dataset_name = os.path.splitext(os.path.basename(data_path))[0]
    
    dataset = load_dataset(data_path)
    survived_count = dataset['Survived'].value_counts()

    labels = ['Not Survived', 'Survived']
    fig, ax = plt.subplots()
    ax.pie(survived_count, labels=labels, autopct='%1.1f%%')
    ax.set_title('Survival Percentage Prediction Overview')
    plt.tight_layout()

    if store_file:
        filename = f"/result/survival_percentage_{dataset_name}.png"
        plt.savefig(filename, dpi=300, bbox_inches="tight")

    buf = BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    base64_string = base64.b64encode(buf.getbuffer()).decode("ascii")

    return f'<img src="data:image/png;base64,{base64_string}" />'




















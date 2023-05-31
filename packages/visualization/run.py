#!/usr/bin/python3

#original code from https://github.com/epi-project/brane-disaster-tweets-example
#code has been modified to be used in our usecase

import ast
import codecs
import os
import sys

import pandas as pd
import json
import yaml

from visualization import (plot_survival_percentage, plot_categorical_attributes, plot_numeric_attributes, plot_correlation_matrix)


def print_output(data: dict):
    """
    Creates a marked section in the standard output
    of the container in order for Brane to isolate the result.

    Parameters
    ----------
    data: `dict`
    Any valid Python dictionary that is YAML serializable.
    """
    print("--> START CAPTURE")
    print(yaml.dump(data))
    print("--> END CAPTURE")




def visualization_action(filepath_submission: str, filepath_train_dataset: str, filepath_test_dataset: str) -> int:
    """
    Create an Html that contains all the plots based on the test
    and submission datasets.

    Parameters
    ----------
    filepath_submission: `str`
    CSV file containing the submission dataset.

    filepath_train_dataset: `str`
    CSV file containing the training dataset.
    
    filepath_test_dataset: `str`
    CSV file containing the test dataset.

    Returns
    -------
    `int` Error code.
    """

    survival_percentage_img = plot_survival_percentage(filepath_submission)
    
    categorical_attributes_img_result = plot_categorical_attributes(filepath_submission, filepath_test_dataset)
    numeric_attributes_img_result = plot_numeric_attributes(filepath_submission, filepath_test_dataset)
    correlation_matrix_img_result = plot_correlation_matrix(filepath_submission, filepath_test_dataset)
    
    categorical_attributes_img = plot_categorical_attributes(filepath_train_dataset)
    numeric_attributes_img = plot_numeric_attributes(filepath_train_dataset)
    correlation_matrix_img = plot_correlation_matrix(filepath_train_dataset)
        
    template_html = codecs.open("./result.html", "r", "utf-8")
    result = template_html.read().format(
        prediction_overview=survival_percentage_img, 
        categorical_attributes_result=categorical_attributes_img_result, 
        numeric_attributes_result=numeric_attributes_img_result,
        correlation_matrix_result=correlation_matrix_img_result,
        categorical_attributes=categorical_attributes_img, 
        numeric_attributes=numeric_attributes_img,
        correlation_matrix=correlation_matrix_img
    )

    try:
        with open("/result/result.html", "w") as f:
            f.write(result)
        return "/result/result.html"
    except IOError as e:
        return ""



def main():
    command = sys.argv[1]
    
    
    
    if command == "visualization_action":
        filepath_submission = f"{json.loads(os.environ['FILEPATH_SUBMISSION'])}/submission.csv"    
        filepath_train_dataset = f"{json.loads(os.environ['FILEPATH_TRAIN_DATASET'])}/dataset.csv"
        filepath_test_dataset = f"{json.loads(os.environ['FILEPATH_TEST_DATASET'])}/dataset.csv"

        output = visualization_action(filepath_submission, filepath_train_dataset, filepath_test_dataset)
        # print_output({"output": output})
        return    
    

    if command == "plot_survival_percentage":
        filepath_submission = f"{json.loads(os.environ['FILEPATH_SUBMISSION'])}/submission.csv"
        filepath_image = plot_survival_percentage(filepath_submission)
        # print_output({"output": output})
        return
    

    if command == "plot_categorical_attributes":
        filepath_train_dataset = f"{json.loads(os.environ['FILEPATH_TRAIN_DATASET'])}/dataset.csv"
        filepath_image = plot_categorical_attributes(filepath_train_dataset)
        # print_output({"output": output})
        return
             

    if command == "plot_numeric_attributes":
        filepath_train_dataset = f"{json.loads(os.environ['FILEPATH_TRAIN_DATASET'])}/dataset.csv"
        filepath_image = plot_numeric_attributes(filepath_train_dataset)
        # print_output({"output": output})
        return

    if command == "plot_correlation_matrix":
        filepath_train_dataset = f"{json.loads(os.environ['FILEPATH_TRAIN_DATASET'])}/dataset.csv"
        filepath_image = plot_correlation_matrix(filepath_train_dataset)
        # print_output({"output": output})
        return  

if __name__ == '__main__':
    main()
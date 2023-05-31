#!/usr/bin/python3

#original code from https://github.com/epi-project/brane-disaster-tweets-example
#code has been modified to be used in our usecase


import os
import sys
import json
import yaml
import pandas as pd

from submission import create_submission
from model import train_LR_model
from preprocess import (clean_data, remove_null_values) 


'''
Entrypoint for the compute package.
'''


def run_dataset_action(cmd: str, filepath: str):
    """
    Runs generic dataset preprocessing action.

    Parameters
    ----------
    cmd: `str`
    The action name.

    filepath: `str`
    The dataset filepath in the DFS.
    """
    return {
        "clean_data": clean_data,"remove_null_values":remove_null_values,
    }[cmd](filepath)


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
    
    

def main():
    command = sys.argv[1]


    if command == "train_LR_model":
        filepath_dataset = f"{json.loads(os.environ['FILEPATH_DATASET'])}/cleaned_dataset.csv"
        filepath_model = train_LR_model(filepath_dataset)
        return

    if command == "create_submission":
        filepath_test_dataset = f"{json.loads(os.environ['FILEPATH_TEST_DATASET'])}/cleaned_dataset.csv"
        filepath_model = f"{json.loads(os.environ['FILEPATH_MODEL'])}/LR_trained_model.pickle"
        filepath_submission = create_submission(filepath_test_dataset, filepath_model)
        return

    filepath_in = json.loads(os.environ["FILEPATH"])
    filepath_out = run_dataset_action(command, filepath_in)


if __name__ == '__main__':
    main()       
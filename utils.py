import os
from joblib import load
import pandas as pd
import json


def retrieve_model_from_folder(folder, model_name):
    model_path = os.path.join(folder, model_name)
    clf = load(model_path) 
    return clf

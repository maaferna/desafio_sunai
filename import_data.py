import pandas as pd
import os


def dowload_data(file_name):
    absolute_path = os.path.dirname(__file__)
    relative_path_production = file_name
    path_production = os.path.join(absolute_path, relative_path_production)

    return pd.read_excel(path_production)

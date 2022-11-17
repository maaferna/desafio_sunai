import pandas as pd
import numpy as np
import os

from import_data import dowload_data
from generate_chart import chart_graph
from result_file import diary_result
def main():
    dir_file = ["find-test-1.xlsx"]
    # Use a breakpoint in the code line below to debug your script.
    try:
        data_production = dowload_data(dir_file[0])
        chart_graph(data_production)
        diary_result(data_production)
        print(data_production)
    except Exception as type_error:
        print(type(type_error))
        print(type_error.args)
        print(type_error)



# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

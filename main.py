import pandas as pd
import numpy as np
import os

from import_data import dowload_data
from generate_chart import chart_graph, graph_result
from result_file import diary_result


def main():
    dir_file = ["data_plantas_python_1_1.xlsx", "data_plantas_python_2.xlsx"]
    # Use a breakpoint in the code line below to debug your script.
    try:
        columns_name_result = ['file_name', 'id_i', 'Minimum', 'Maximum', 'Mean',
                               'Sum']
        df_result = pd.DataFrame(columns=columns_name_result)
        j = 0
        suma = 0
        while j <= len(dir_file) - 1:
            dir_id_i = dowload_data(dir_file[j])['id_i'].unique()
            df = dowload_data(dir_file[j])
            print(dir_id_i)

            for i in dir_id_i:
                data_production = df.query("id_i == @i")
                minimum = data_production["active_energy_im"].min()
                maximum = data_production["active_energy_im"].max()
                mean = round(data_production["active_energy_im"].mean(), 2)
                suma = data_production["active_energy_im"].sum()

                print(minimum, maximum, mean, suma)
                chart_graph(data_production, i, dir_file[j])
                diary_result(df_result, dir_file[j], i, minimum, maximum, mean, suma)

                print(data_production)
            j += 1

        df_result.to_csv('kpi_diario.txt', header=True, index=None, sep=' ')

        graph_result(df_result)


    except Exception as type_error:
        print(type(type_error))
        print(type_error.args)
        print(type_error)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

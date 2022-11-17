
def diary_result(data_result):
    data_result.to_csv(r'result\kpi_diario.txt', header=None, index=None, sep=' ', mode='a')
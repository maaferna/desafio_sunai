
def diary_result(df_result, file_name, id_i, minimum, maximum, mean):
    idx_add = len(df_result)
    df_result.loc[idx_add + 1, 'file_name'] = file_name
    df_result.loc[idx_add + 1, 'id_i'] = id_i
    df_result.loc[idx_add + 1, 'Minimum'] = minimum
    df_result.loc[idx_add + 1, 'Maximum'] = maximum
    df_result.loc[idx_add + 1, 'Mean'] = mean

    return df_result
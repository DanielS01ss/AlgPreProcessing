import pandas as pd
import json


def constant_value_imputation(dataset, columns, constant_values):
    df = dataset
    for i in range(len(columns)):
        if columns[i] in df:
            df[columns[i]].fillna(constant_values[i], inplace=True)

    return df

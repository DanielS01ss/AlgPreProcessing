import pandas as pd
import json


def mode_imputation(dataset, columns):
    df = pd.DataFrame(dataset)
    for column in columns:
        mode_value = df[column].mode()[0]
        df[column].fillna(mode_value, inplace=True)

    return df

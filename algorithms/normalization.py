import json
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np


def normalization(dataset, columns):
    df = pd.DataFrame(dataset)
    scaler = MinMaxScaler()
    result_df = dataset
    for column in columns:
        if column in df.columns:
            interest_column = np.array(df[column])
            df.drop(columns=[column], inplace=True)
            interest_column = interest_column.reshape(-1, 1)
            normalized_data = scaler.fit_transform(interest_column)
            df[column] = normalized_data

    parsed_df = json.dumps(df.to_dict(orient='records'))

    return parsed_df

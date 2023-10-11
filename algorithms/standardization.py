from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import json


def standardization(data, columns):
    df = pd.DataFrame(data)
    scaler = StandardScaler()

    for column in columns:
        if column in df.columns:
            interest_column = np.array(df[column])
            df.drop(columns=[column], inplace=True)
            interest_column = interest_column.reshape(-1, 1)
            normalized_data = scaler.fit_transform(interest_column)
            df[column] = normalized_data

    parsed_df = json.dumps(df.to_dict(orient='records'))
    return parsed_df

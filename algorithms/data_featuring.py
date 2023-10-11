import pandas as pd
import json


def data_featuring(data, columns):
    df = pd.DataFrame(data)
    for col in columns:
        if col in df.columns:
            df.drop(columns=[col], inplace=True)

    df_dict = json.dumps(df.to_dict(orient='records'))
    return df_dict

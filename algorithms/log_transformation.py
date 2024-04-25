import pandas as pd
import numpy as np
from scipy import stats
import json

def log_transformation_algorithm(data, columns):
    data1 = json.loads(data)
    df = pd.DataFrame(data1)
    for col in columns:
        df[col["column_name"]] = np.log(df[col["column_name"]])
       
    return df
import pandas as pd
from scipy import stats
import json

def remove_outliers_column(df, column_name):
    upper_limit = df[column_name].mean() + 3*df[column_name].std()
    lower_limit = df[column_name].mean() + 3*df[column_name].std()
    new_df = df.loc[(df[column_name] < upper_limit) | (df[column_name] > lower_limit)]
    return new_df

def outlier_removal_algorithm(data, columns):
    data1 = json.loads(data)
    df = pd.DataFrame(data1)
    dataset = df
    for col in columns:
        
        dataset = remove_outliers_column(dataset, col['column_name'])
    
    return dataset

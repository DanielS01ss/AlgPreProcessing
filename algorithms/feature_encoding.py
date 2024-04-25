import pandas as pd
from sklearn.preprocessing import LabelEncoder

def one_hot_encoding(df, column):
    df_encoded = pd.get_dummies(df, columns=[column])
    df.drop(columns=[column], inplace=True)
    df_final = pd.concat([df, df_encoded], axis=1)
    return df_final

def label_encoding(df, column):
    label_encoder = LabelEncoder()
    df[column] = label_encoder.fit_transform(df[column])
    return df

def target_encoding(df, column, target, weight=0.5):

    mean_target = df[target].mean()
    agg = df.groupby(column)[target].agg(['count', 'mean'])
    counts = agg['count']
    means = agg['mean']
    encoded_column = (counts * means + weight * mean_target) / (counts + weight)
    return df[column].map(encoded_column)
    


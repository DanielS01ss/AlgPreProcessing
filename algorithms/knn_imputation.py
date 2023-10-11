from sklearn.impute import KNNImputer
import pandas as pd
import json


def knn_imputation(dataset, k_neighbours=2):
    imputer = KNNImputer(n_neighbors=k_neighbours)
    df = dataset
    df_imputed = imputer.fit_transform(df)
    df_imputed = pd.DataFrame(df_imputed, columns=df.columns)

    return df_imputed



from sklearn.linear_model import LinearRegression
import pandas as pd
import json


def regression_imputation(dataset, target_columns, feature_columns):
    df = dataset
    for column in feature_columns:
        if column not in df:
            return df
        contains_nan = df[column].isna().any()
        if contains_nan:
            return df
    for target_column in target_columns:
        if target_column not in df:
            return df
        complete_data = df.dropna(subset=[target_column])
        incomplete_data = df[df[target_column].isna()]
        if len(incomplete_data) == 0:
            return df
        print(incomplete_data)
        # Fit a linear regression model
        model = LinearRegression()
        model.fit(complete_data[feature_columns], complete_data[target_column])

        predictions = model.predict(incomplete_data[feature_columns])
        if len(predictions) == 0:
            continue

        df.loc[df[target_column].isna(), target_column] = predictions

    return df

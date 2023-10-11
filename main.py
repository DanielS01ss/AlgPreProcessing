from fastapi import FastAPI, HTTPException
from algorithms.data_featuring import data_featuring
from models.data_featuring_model import DataFeaturing
from models.normalization_model import Normalization
from models.standardization_model import Standardization
from algorithms.standardization import standardization
from algorithms.normalization import normalization
from algorithms.mode_imputation import mode_imputation
from algorithms.knn_imputation import knn_imputation
from algorithms.constant_value_imputation import constant_value_imputation
from algorithms.regression_imputation import regression_imputation
from models.imputation_model import Imputation
import pandas as pd
import json
import pandas as pd
from algorithms.data_featuring import data_featuring

app = FastAPI()


@app.post("/data-featuring")
def data_featuring_req(req: DataFeaturing):
    if len(req.columns) == 0:
        raise HTTPException(status_code=400, detail="Please specify columns you want to remove!")
    proccessed_data = data_featuring(req.data, req.columns)

    return proccessed_data


@app.post("/normalization")
def data_normalization_req(req: Normalization):
    if len(req.columns) == 0:
        raise HTTPException(status_code=400, detail="Please specify columns you want to remove!")
    dataset = req.data
    columns = req.columns
    dataset = normalization(dataset, columns)
    return dataset


@app.post("/standardization")
def data_standardization_req(req: Standardization):
    if len(req.columns) == 0:
        raise HTTPException(status_code=400, detail="Please specify columns you want to remove!")
    dataset = req.data
    columns = req.columns
    dataset = standardization(dataset, columns)

    return dataset


@app.post("/data-imputation")
def data_imputation_req(req: Imputation):
    dataset = req.data
    dataset = pd.DataFrame(dataset)

    if req.knn_imputation:
        dataset = knn_imputation(dataset)
    if req.mode_imputation_columns and len(req.mode_imputation_columns) > 0:
        dataset = mode_imputation(dataset, req.mode_imputation_columns)
    if req.constant_value_imputation_columns and len(req.constant_value_imputation_columns):
        if len(req.constant_value_imputation_columns) != len(req.constant_value_imputation_values):
            raise HTTPException(status_code=400, detail="You should specify a value for each column!")
        dataset = constant_value_imputation(dataset, req.constant_value_imputation_columns, req.constant_value_imputation_values)
    if req.regression_value_imputation_feature_columns and req.regression_value_imputation_target_columns and len(req.regression_value_imputation_target_columns) != 0 and len(req.regression_value_imputation_feature_columns) != 0:
        dataset = regression_imputation(dataset, req.regression_value_imputation_target_columns, req.regression_value_imputation_feature_columns)

    dataset = json.dumps(dataset.to_dict(orient='records'))
    return dataset

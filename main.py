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
from algorithms.outlier_removal_algorithm import outlier_removal_algorithm
from algorithms.log_transformation import log_transformation_algorithm
from algorithms.feature_encoding import one_hot_encoding
from algorithms.feature_encoding import label_encoding
from algorithms.feature_encoding import target_encoding
from models.imputation_model import Imputation
from models.outlier_removal import OutlierRemoval
from models.feature_encoding import FeatureEncoding
from fastapi.responses import JSONResponse
import uvicorn
import pandas as pd
import json
import pandas as pd
from algorithms.data_featuring import data_featuring

app = FastAPI()


@app.get("/hello")
def tester():
      return JSONResponse(content={"message": "Hello World!"}, status_code=200)

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

@app.post("/outlier-removal")
def data_standardization_req(req: OutlierRemoval):
    
    if len(req.columns) == 0:
        raise HTTPException(status_code=400, detail="Please specify columns you want to remove!")
    dataset = req.data
    columns = req.columns
    dataset = outlier_removal_algorithm(dataset, columns)
    df_dict = json.dumps(dataset.to_dict(orient='records'))
    return df_dict

@app.post("/log-transformation")
def data_log_transformation_req(req: OutlierRemoval):
    if len(req.columns) == 0:
        raise HTTPException(status_code=400, detail="Please specify columns you want to remove!")
    dataset = req.data
    columns = req.columns
    dataset = log_transformation_algorithm(dataset, columns)
    df_dict = json.dumps(dataset.to_dict(orient='records'))
  
    return df_dict

@app.post("/data-imputation")
def data_imputation_req(req: Imputation):
    dataset = req.data
    dataset = json.loads(dataset)
    dataset = pd.DataFrame(dataset)
    
    if req.knn_imputation:
        dataset = knn_imputation(dataset)
    if req.constant_value_imputation_columns and len(req.constant_value_imputation_columns):
        if len(req.constant_value_imputation_columns) != len(req.constant_value_imputation_values):
            raise HTTPException(status_code=400, detail="You should specify a value for each column!")
        dataset = constant_value_imputation(dataset, req.constant_value_imputation_columns, req.constant_value_imputation_values)

    dataset = json.dumps(dataset.to_dict(orient='records'))
    return dataset

@app.post("/feature-encoding")
def data_imputation_req(req: FeatureEncoding):
    dataset = req.data
    dataset = json.loads(dataset)
    dataset = pd.DataFrame(dataset)
    
    print("columns:")
    print(req.columns)
    #logica 
    if req.encoding_type == "Label Encoding":
        for column in req.columns:
            dataset = label_encoding(dataset,column["column_name"])

    elif req.encoding_type == "Target Encoding":
        for column in req.columns:
            # dataset[column["column_name"]] = target_encoding(dataset,column["column_name"],req.target_column)
            updated_dataset = target_encoding(dataset,column["column_name"],req.target_column)
            continue
    elif req.encoding_type == "One Hot Encoding":
        for column in req.columns:
            dataset = one_hot_encoding(dataset,column["column_name"])

    dataset = json.dumps(dataset.to_dict(orient='records'))
    return dataset


if __name__ == '__main__':
    uvicorn.run(app,host='0.0.0.0', port=8001)
from typing import List, Optional,Any
from pydantic import BaseModel


class Imputation(BaseModel):
    data: Any
    knn_imputation: Any
    constant_value_imputation_columns: Any
    constant_value_imputation_values: Any
    regression_value_imputation_target_columns: Any
    regression_value_imputation_feature_columns: Any


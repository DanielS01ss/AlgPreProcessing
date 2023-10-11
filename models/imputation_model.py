from typing import List, Optional
from pydantic import BaseModel


class Imputation(BaseModel):
    data: List
    knn_imputation: bool
    mode_imputation_columns: Optional[List]
    constant_value_imputation_columns: Optional[List]
    constant_value_imputation_values: Optional[List]
    regression_value_imputation_target_columns: Optional[List]
    regression_value_imputation_feature_columns: Optional[List]


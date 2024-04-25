from typing import List, Optional,Any
from pydantic import BaseModel


class FeatureEncoding(BaseModel):
    data: Any
    encoding_type: Any
    target_column: Any
    columns: Any


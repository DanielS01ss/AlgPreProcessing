from typing import List, Dict,Union,Any

from pydantic import BaseModel


class DataFeaturing(BaseModel):
    columns: List[str]
    data: Any

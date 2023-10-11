from typing import List

from pydantic import BaseModel


class DataFeaturing(BaseModel):
    columns: List
    data: List

from typing import List

from pydantic import BaseModel


class Standardization(BaseModel):
    columns: List
    data: List

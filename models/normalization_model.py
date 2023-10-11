from typing import List

from pydantic import BaseModel


class Normalization(BaseModel):
    columns: List
    data: List

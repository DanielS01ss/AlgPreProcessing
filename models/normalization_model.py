from typing import List, Any

from pydantic import BaseModel


class Normalization(BaseModel):
    columns: Any
    data: Any

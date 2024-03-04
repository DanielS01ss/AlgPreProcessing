from typing import List, Any

from pydantic import BaseModel


class Standardization(BaseModel):
    columns: Any
    data: Any

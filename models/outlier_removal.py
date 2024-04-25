from typing import List, Any

from pydantic import BaseModel


class OutlierRemoval(BaseModel):
    columns: Any
    data: Any

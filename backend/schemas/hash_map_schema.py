from pydantic import BaseModel
from typing import Optional, List, Tuple


class KeyValuePair(BaseModel):
    key: str
    value: str


class HashMapResponse(BaseModel):
    size: int
    data: List[Optional[KeyValuePair]]

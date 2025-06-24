from pydantic import BaseModel


class SortItem(BaseModel):
    value: list[int]
    algorithm: str

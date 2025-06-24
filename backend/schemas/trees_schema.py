from pydantic import BaseModel


class TreeItem(BaseModel):
    value: int

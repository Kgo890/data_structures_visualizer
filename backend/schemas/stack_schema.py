from pydantic import BaseModel


class StackItem(BaseModel):
    value: int

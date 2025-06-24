from pydantic import BaseModel


class QueueItem(BaseModel):
    value: int

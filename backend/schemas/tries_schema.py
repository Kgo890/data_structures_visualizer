from pydantic import BaseModel
from typing import Dict


class TriesItems(BaseModel):
    value: str


class AdvancedMatchRequest(BaseModel):
    document: str
    variations: Dict[str, str]

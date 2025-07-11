from pydantic import BaseModel, Field, model_validator


class NodeItem(BaseModel):
    node: int = Field(..., ge=0, description="Must be a non-negative integer")


class EdgeItem(BaseModel):
    first_node: int = Field(..., ge=0, description="Must be a non-negative integer")
    second_node: int = Field(..., ge=0, description="Must be a non-negative integer")

    @model_validator(mode='before')
    def no_self_edge(cls, data):
        if data['first_node'] == data['second_node']:
            raise ValueError("Cannot create an edge from a node to itself")
        return data

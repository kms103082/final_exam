from pydantic import BaseModel

class UserInput(BaseModel):
    method : str
    requirement : str
    location : str
    level : str

# Data validation -- 

from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

class User(BaseModel):
    name:str
    gmail:str
    age:int = Field(..., gt=0, le=120)
    
    @field_validator("name")
    def name_must_not_be_empty(cls, v):
        if not v:
            raise ValueError("Name must not be empty")
        return v

app = FastAPI()

@app.post("/register/")
async def register_user(user:User):
    return user
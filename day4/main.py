# Request and Response -- 

from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

# class User(BaseModel):
#     name:str
#     age:int
#     number:int

@app.get("/")
def read_root():
    return{"message":"hello rohan all good."}

# request section
# @app.post("/user/")
# async def create_user(user:User):
#     return{user.name,user.age,user.number}

# responce section 
# @app.get("/users/{user_id}",response_model=User)
# async def getUser(user_id:int):
#     return{"name":"Rohan pandey","age":21,"number":234}



# Example

class User(BaseModel):
    name:str
    age:int = Field(..., gt=0, le=120)

    @field_validator("name")
    def name_must_not_be_empty(cls, v):
        if not v:
            raise ValueError("Name must not be empty")
        return v

@app.post("/users/")
async def create_user(user:User):
    u={"name":user.name, "age":user.age}
    return u
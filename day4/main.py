# Request and Response -- 

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    number:int

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
#     return{"name":"Rohan pandey","age":21}



# Example
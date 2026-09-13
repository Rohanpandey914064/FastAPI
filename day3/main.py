# path parameters and Query parameters

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return{"message":"hello rohan all good."}

# @app.get("/users/{user_id}")
# def read_users(user_id:int):
#     return{"Rohan user id is",user_id}

# @app.get("/users/{name}")
# def read_users(name:str):
#     return{"Rohan user id is",name}

# @app.get("/users/")
# def read_users(user_id:int,name:str):
#     return{"id":user_id,"name":name}

@app.get("/users/{user_id}/details")
def read_users(user_id:int,include_email:bool=False):
    if include_email:
        return{"id":user_id, "include_email":"email available bro"}
    else:
        return{"id":user_id,"include_email":"email not available bro"}
    
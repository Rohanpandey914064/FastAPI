# Request and Response -- 

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return{"message":"hello rohan all good."}

    
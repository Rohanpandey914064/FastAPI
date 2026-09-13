# CURD opration

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return{"message":"hello rohan all good."}

@app.post("/items/")
def create_item(name: str,price: float):
    return{"name":name , "price":price}

@app.put("/items/{id}")
def update_item(id: int,name: str,price: float):
    return{"id":id,"name":name,"price":price}

@app.delete("/items/{id}")
def delete_item(id:int):
    return{"id":f"item {id} deleted succesfully"}
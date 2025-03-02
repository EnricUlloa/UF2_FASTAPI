from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "message": f"Has solicitado el item {item_id}"}

from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    stock: int
    category: str

@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item creado con éxito", "item": item}

from fastapi import HTTPException

items = {1: {"name": "Laptop", "price": 1000}}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return {"item_id": item_id, "item": items[item_id]}

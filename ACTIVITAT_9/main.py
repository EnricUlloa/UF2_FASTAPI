from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from typing import List
from db_connect.database import SessionLocal
from crud.user import read_users

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Item(BaseModel):
    name: str = Field(..., title="Item Name", max_length=50)
    description: str = Field(None, title="Description", max_length=200)
    price: float = Field(..., gt=0, description="Price must be greater than zero")
    tax: float = Field(default=0, le=50, description="Tax must be 50 or less")

@app.post("/items/")
async def create_item(item: Item):
    return {"message": "Item received", "data": item}


@app.get("/users/")
def get_users(db=Depends(get_db)):
    return read_users(db)


class Feature(BaseModel):
    name: str
    enabled: bool


class Product(BaseModel):
    name: str
    price: float
    features: List[Feature]  
    
@app.post("/products/")
async def create_product(product: Product):
    return {"message": "Product received", "data": product}


@app.get("/")
def read_root():
    return {"message": "Bienvenido a mi API con FastAPI"}

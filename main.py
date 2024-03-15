from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union, Optional
from routers import products, users

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, query: Union[str, None] = None):
    return {"item_id": item_id, "query": query}


@app.put("/items/{item_id}")
def update_item(item_id: Optional[int], item: Item):
    return {"item_name": item.name, "item_id": item_id}

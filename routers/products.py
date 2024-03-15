from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Union, List

router = APIRouter(prefix="/products", tags=["products"])

# Init server: uvicorn users:app --reload

# Entity User

class Product(BaseModel):
  id: int
  name: str
  price: int
  has_discount: Union[bool, None] = None


product_list = [
  Product(id=1, name="Tenis", price=329932),
  Product(id=2, name="Camisa", price=399232),
  Product(id=3, name="Pantalon", price= 238923),
]

# PATH
@router.get("/", response_model=List[Product], status_code=status.HTTP_200_OK)
async def products():
  try:
    return product_list
  except:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
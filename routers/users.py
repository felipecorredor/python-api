from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Union, List

router = APIRouter(prefix="/users", tags=["users"])

# Init server: uvicorn users:app --reload

# Entity User

class User(BaseModel):
  id: int
  name: str
  surname: str
  url: Union[str, None] = None
  age: int


user_list = [
  User(id=1, name="Felipe", surname="pipe", url="https", age=23),
  User(id=2, name="Juan", surname="juan", url="https://juan.dev", age=35),
]

# PATH
@router.get("/{id}", response_model=User)
async def user_by_id(id: int):
  if search_user(id):
    return search_user(id)
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

# QUERY
@router.get("/query", response_model=User, status_code=status.HTTP_200_OK)
async def user_query(query: Union[int, None] = None):
  if search_user(query):
    return search_user(query)

  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
 

@router.get("/", response_model=List[User], status_code=status.HTTP_200_OK)
async def products():
  try:
    return user_list
  except:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def add_user(user: User):
  if search_user(user.id):
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User has been added previously")

  user_list.append(user)
  return user

@router.put("/{id}", response_model=User, status_code=status.HTTP_200_OK)
async def update_user(id: int, user: User):
    for index, saved_user in enumerate(user_list):
       if saved_user.id == id:
          user_list[index] = user
          return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

# @router.put("/user/{id}", status_code=status.HTTP_200_OK)
# async def update_user(id: int, user: User):
#     try:
#         saved_user = next(saved_user for saved_user in user_list if saved_user.id == id)
#         saved_user.name = user.name
#         saved_user.email = user.email
#         # Actualizar otros campos según sea necesario
#         return saved_user
#     except StopIteration:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
 
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: int):
  for index, saved_user in enumerate(user_list):
   if saved_user.id == id:
      del user_list[index]
      return {}
      
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

def search_user(id: int):
  filtered_users = filter(lambda user:user.id == id, user_list)
  for user in filtered_users:
      return user
  return None
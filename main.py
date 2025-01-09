from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
  name: str
  email: str

@app.get('/')
async def read_root():
  return {'message': 'Hello, World!'}

@app.get('/greet/')
async def greet(username: Optional [str] = 'User'):
  return {'message': f'Hello, {username}'}


@app.get('/greet/{username}')
async def greet(username: str):
  return {'message': f'Hello, {username}'}

user_list = [
   "Jerry",
   "Joey",
   "Phil"
] 

users: list[User] = []

@app.get('/search')
async def search(username: str):
  if username in user_list:
    return {'message', f'details for user {username}'}
  return {'message', 'user not found'}

@app.post('/create_user')
async def create_user(user_data: User):
  new_user = {
    'name': user_data.name,
    'email': user_data.email
  }
  
  users.append(new_user)
  
  return {"message":"User Created successfully","user":new_user}
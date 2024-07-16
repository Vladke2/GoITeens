from fastapi import FastAPI, HTTPException
from .models import User, Item


app = FastAPI()


users = []
items = []


@app.get('/')
def main():
    return "Welcome to the FastAPI project"


@app.post('/users/')
def create_user(user: User):
    user_id = len(user) + 1
    new_user = User(id=user_id, **user.dict())
    users.append(new_user)
    return new_user


@app.get('/users/{user_id}')
def get_user(user_id: int):
    for user in users:
        if user == user_id:
            return user
    raise HTTPException(status_code=404, detail='User not found')


@app.post('/items/')
def create_item(item: Item):
    item_id = len(item) + 1
    new_item = Item(id=item_id, **item.dict())
    items.append(new_item)
    return new_item


@app.get('/items/{item_id}')
def get_item(item_id: int):
    for item in items:
        if item == item_id:
            return item
    raise HTTPException(status_code=404, detail='Item not found')

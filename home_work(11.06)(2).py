from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Union


app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    age: int = None
    email: EmailStr


class Address(BaseModel):
    user_id: int
    address: str
    type: Union[str, None] = None


users = []
addresses = []


@app.post('/users/', status_code=201)
def create_user(user: User):
    users.append(user)
    return user


@app.get('/users/')
def all_users():
    return users


@app.post('/addresses/')
def create_address(address: Address):
    addresses.append(address)
    return address


@app.get('/addresses/')
def all_addresses():
    return addresses

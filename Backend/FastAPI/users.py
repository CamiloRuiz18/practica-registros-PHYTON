#Entidad para Usuarios

from fastapi import FastAPI
from pydantic import BaseModel , EmailStr #Para trabajar entidades

app = FastAPI()

class UsersRegister(BaseModel):
    id: int
    name: str
    surname: str
    phone: str
    email: EmailStr #Valida el formato no que el correo exista
    password: str

data_base_users = [
    UsersRegister(id=1, name="Andres", surname="Ruiz", phone="3107881033", email="ruiz165@gmail.com", password="Camilo123@"),
    UsersRegister(id=2, name="Natalia", surname="Romero", phone="3053508417", email="natalia18@gmail.com", password="Natalia18@"),
    UsersRegister(id=3, name="Salome", surname="Rios", phone="300000003", email="salome23@gmail.com", password="Salome23@")
]

@app.get("/users")
async def users():
    return data_base_users

#PATH
@app.get("/users/{id}")
async def user(id:int):
    return search_user

#QUERY
@app.get("/users/")
async def user(id:int):
    return search_user


def search_user(id:int):
    
    return
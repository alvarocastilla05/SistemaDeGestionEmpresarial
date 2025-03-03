from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Entidad user
class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users = [User(name = "Brais", surname ="moure", url = "https://moure.dev", age = 35),
         User(name = "Lucas", surname ="Falla", url = "https://moure.dev", age = 35),
         User(name = "Álvaro", surname ="Castilla", url = "https://moure.dev", age = 35)]


@app.get("/usersjson")
async def usersjson():
    return [{"name": "Brais", "surname": "moure", "url": "https://moure.dev", "age": 35},
            {"name": "Lucas", "surname": "Falla", "url": "https://moure.dev", "age": 35},
            {"name": "Álvaro", "surname": "Castilla", "url": "https://moure.dev","age": 35}]

@app.get("/users")
async def users():
    return users



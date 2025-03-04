from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id = 1, name = "Brais", surname ="moure", url = "https://moure.dev", age = 35),
         User(id = 2, name = "Lucas", surname ="Falla", url = "https://moure.dev", age = 35),
         User(id = 3, name = "Álvaro", surname ="Castilla", url = "https://moure.dev", age = 35)]


@app.get("/usersjson")
async def usersjson():
    return [{"name": "Brais", "surname": "moure", "url": "https://moure.dev", "age": 35},
            {"name": "Lucas", "surname": "Falla", "url": "https://moure.dev", "age": 35},
            {"name": "Álvaro", "surname": "Castilla", "url": "https://moure.dev","age": 35}]

@app.get("/users")
async def users():
    return users_list


@app.get("/users/{id}")
async def user(id: int):
    return search_user(id)


@app.get("/userquery/")
async def userquery(id: int):
    return search_user(id)



@app.post("/user/")
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "User already exists"}
    else:
        users_list.append(user)
        return user


@app.put("/user/")
async def update_user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            return user

    if not found:
        return {"error": "User not found"}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "User not found"}





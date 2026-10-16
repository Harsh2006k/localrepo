from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, product: str | None = None):
    return {"item_id": item_id, "item": product}

#Mock Data
users = [
    {"id":1, "name":"John", "email":"john@example.com"},
    {"id":2, "name":"Jane", "email":"jane@example.com"},
    {"id":3, "name":"Bob", "email":"bob@example.com"}
]


@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

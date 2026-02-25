from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_fastapi():
    return '{"message": "API FastAPI est opérationelle"}'


@app.get("/users")
def get_users():
    return [{"id": 1, "name": "Charlie"},
            {"id": 2, "name": "Alice"},
            {"id": 3, "name": "Bob"}
    ]

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id}

@app.get("/search")
def search(name: str | None = None):
    return {"search": name}
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    title: str
    completed: bool = False


@app.get("/")
def home():
    return {"message": "Farm Todo API Running"}


@app.get("/todos")
def get_todos():
    return todos


@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo added", "todo": todo}
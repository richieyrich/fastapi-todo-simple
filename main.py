# Import libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Create a FastAPI instance
app = FastAPI()

# Pydantic model for the todo item
class Todo(BaseModel):
    id: int
    item: str

# empty list to store the todo items
todos = []

# Define the routes
@app.get("/todos", response_model=List[Todo])
async def read_todos():
    return todos

@app.post("/todos", response_model=Todo)
async def create_todo(todo: Todo):
    todos.append(todo)
    return todo

@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo: Todo):
    for i in range(len(todos)):
        if todos[i].id == todo_id:
            todos[i] = todo
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}", response_model=Todo)
async def delete_todo(todo_id: int):
    for i in range(len(todos)):
        if todos[i].id == todo_id:
            return todos.pop(i)
    raise HTTPException(status_code=404, detail="Todo not found")

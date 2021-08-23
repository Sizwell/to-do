from sqlalchemy import schema
import to_do.crud
import to_do.models
import to_do.schemas
from fastapi import Depends 
from fastapi import FastAPI
from fastapi import HTTPException
from to_do.db import engine
from to_do.db import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user
from typing import List


to_do.models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create User
@app.post("/users", response_model=to_do.schemas.User)
def create_user(user: to_do.schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = to_do.crud.create_user(db, user)
    return db_user


# Read all users from the Users table
@app.get("/users", response_model=List[to_do.schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = to_do.crud.get_all_users(db, skip=skip, limit=limit)
    return users


# Read One User by ID from the Users table
@app.get("/users/{user_id}", response_model=to_do.schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = to_do.crud.get_user(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# Update user name and Surname 
@app.put("/update_user_details")
def update_user(id: int, update_param: to_do.schemas.UpdateUser, db: Session = Depends(get_db)):
    details = to_do.crud.get_user(db=db, user_id=id)

    if not details:
        raise HTTPException(status_code=404, detail=f"No record to update")

    return to_do.crud.update_user_details(db=db, details=update_param, id=id)    


# Delete User from Users table
@app.delete("/delete_user")
def delete_user_by_id(id: int, db: Session = Depends(get_db)):
    details = to_do.crud.get_user(db=db, user_id=id)

    if not details:
        raise HTTPException(status_code=404, detail=f"No User record found to delete")

    try:
        to_do.crud.delete_user(db=db, user_id=id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "Successfully deleted User record"}


# Create a new task and insert into tasks table 
@app.post("/create_user_task")
def create_task(user_id: int, todo: to_do.schemas.TaskCreate, db: Session = Depends(get_db)):
    db_todo = to_do.crud.create_user_todo(db, todo, user_id=user_id)
    return db_todo


@app.post("/create_todo")
def create_todo(todo: to_do.schemas.TaskCreate, db: Session = Depends(get_db)):
    db_todo = to_do.crud.create_todo2(db, todo)
    return db_todo


# Get all the tasks in the Tasks table
@app.get("/read_task")
def read_task(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = to_do.crud.get_todos(db, skip=skip, limit=limit)
    return tasks
    

# Get 1 task by ID from tasks table
@app.get("/read_task/{id}")
def read_task(user_id: int, db: Session = Depends(get_db)):
    db_task = to_do.crud.get_todo_by_id(db, user_id=user_id)

    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


# Update Task
@app.put("/update_task_details")
def update_task_details(id: int, update_param: to_do.schemas.UpdateTask, db: Session = Depends(get_db)):
    details = to_do.crud.get_todo_by_id(db=db, user_id=id)

    if not details:
        raise HTTPException(status_code=404, detail=f"No record to update")

    return to_do.crud.update_task_details(db=db, details=update_param, id=id)    


# Delete Task from Tasks table
@app.delete("/delete_task")
def delete_task_by_id(id: int, db: Session = Depends(get_db)):
    details = to_do.crud.get_todo_by_id(db=db, user_id=id)

    if not details:
        raise HTTPException(status_code=404, detail=f"No record Task found to delete")

    try:
        to_do.crud.delete_task(db=db, task_id=id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "Successfully deleted Task record"}            


# @app.post("/create_user_task")
# def create_task(user_id: int, todo: to_do.schemas.TaskCreate, db: Session = Depends(get_db)):
#     db_todo = to_do.crud.create_user_todo(db, todo, user_id=user_id)
#     return db_todo

# @app.put("/update_task_details")
# def update_task_details(id: int, update_param: to_do.schemas.UpdateTask, db: Session = Depends(get_db)):
#     details = to_do.crud.get_todo_by_id(db=db, user_id=id)

#     if not details:
#         raise HTTPException(status_code=404, detail=f"No record to update")

#     return to_do.crud.update_task_details(db=db, details=update_param, id=id)    


@app.put("/assign_user_task")
def assign_user_task(id: int, update_param: to_do.schemas.UpdateUserTask, db: Session = Depends(get_db)):
    details = to_do.crud.get_todo_by_id(db=db, user_id=id)

    if not details:
        raise HTTPException(status_code=406, detail=f"Cannot assign user to task")
    return to_do.crud.update_task_details(db=db, details=update_param, id=id)    

    # db_todo = to_do.crud.create_user_todo(db, todo, user_id=user_id)
    # return db_todo
    pass
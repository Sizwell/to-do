import to_do.crud
import to_do.models
import to_do.schemas
from fastapi import Depends 
from fastapi import FastAPI
from fastapi import HTTPException
from to_do.db import engine
from to_do.db import SessionLocal
from sqlalchemy.orm import Session
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


@app.post("/users", response_model=to_do.schemas.User)
def create_user(user: to_do.schemas.UserCreate, db: Session = Depends(get_db)):
    """ Create a new User """

    db_user = to_do.crud.create_user(db, user)
    return db_user


@app.get("/users", response_model=List[to_do.schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """ Read all users from the users table """

    users = to_do.crud.get_all_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=to_do.schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """ Read a specific user by providing a their ID """

    db_user = to_do.crud.get_user(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.put("/update_user_details")
def update_user(id: int, update_param: to_do.schemas.UpdateUser, db: Session = Depends(get_db)):
    """ 
    Update user details by providing the ID of an existing user.
    If the user does not exist in the database, an exception will be raised.

    """

    details = to_do.crud.get_user(db=db, user_id=id)

    if not details:
        raise HTTPException(status_code=404, detail=f"No record to update")

    return to_do.crud.update_user_details(db=db, details=update_param, id=id)    


@app.delete("/delete_user")
def delete_user_by_id(id: int, db: Session = Depends(get_db)):
    """ 
    Delete a user from the database by providing the user ID.
    If the user_id does not exist, an exception will be raised

    """
    
    details = to_do.crud.get_user(db=db, user_id=id)

    if not details:
        raise HTTPException(status_code=404, detail=f"No User record found to delete")

    try:
        to_do.crud.delete_user(db=db, user_id=id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "Successfully deleted User record"}


@app.post("/create_user_task")
def create_user_task(user_id: int, todo: to_do.schemas.TaskCreate, db: Session = Depends(get_db)):
    """ Create a new task which will be assigned to an existing user """

    db_todo = to_do.crud.create_user_task(db, todo, user_id=user_id)
    return db_todo


@app.post("/create_task")
def create_task(todo: to_do.schemas.TaskCreate, db: Session = Depends(get_db)):
    """ 
    Create a new task which at this point will not be assigned to 
    any owner. The owner_id will be none
    
    """

    db_todo = to_do.crud.create_task(db, todo)
    return db_todo


@app.get("/read_task")
def read_task(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """ Read all tasks from the database """

    tasks = to_do.crud.get_todos(db, skip=skip, limit=limit)
    return tasks
    

@app.get("/read_task/{id}")
def read_task(user_id: int, db: Session = Depends(get_db)):
    """ 
    Read a specific task from the databse using its
    primary key

    """

    db_task = to_do.crud.get_todo_by_id(db, user_id=user_id)

    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


# Update Task
@app.put("/update_task_details")
def update_task_details(id: int, update_param: to_do.schemas.UpdateUserTask, db: Session = Depends(get_db)):
    """ 
    Update the contents of a task and also update the status of the task
    which can either set 'done' to true or false    
    
    """

    details = to_do.crud.get_todo_by_id(db=db, user_id=id)

    if not details:
        raise HTTPException(status_code=404, detail=f"No record to update")

    return to_do.crud.update_task_details(db=db, details=update_param, id=id)    


@app.delete("/delete_task")
def delete_task_by_id(id: int, db: Session = Depends(get_db)):
    """ Delete a task from the Tasks table using the task_id """

    details = to_do.crud.get_todo_by_id(db=db, user_id=id)

    if not details:
        raise HTTPException(status_code=404, detail=f"No record Task found to delete")

    try:
        to_do.crud.delete_task(db=db, task_id=id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "Successfully deleted Task record"}            


@app.put("/assign_task_to_user")
def assign_user_task(task_id: int, update_param: to_do.schemas.UpdateTask, db: Session = Depends(get_db)):
    """ Assign a task with a null owner_id to an existing user """

    details = to_do.crud.get_todo_by_id(db=db, user_id=task_id)

    if not details:
        raise HTTPException(status_code=406, detail=f"Cannot assign User to Task")

    return to_do.crud.update_task(db=db, details=update_param, id=task_id)    

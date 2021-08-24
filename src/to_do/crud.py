import to_do.models
import to_do.schemas
from sqlalchemy.orm import Session


def create_user(db: Session, user: to_do.schemas.UserCreate):
    db_user = to_do.models.User(name=user.name, surname=user.surname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(to_do.models.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.query(to_do.models.User).filter(to_do.models.User.id == user_id).first()


def update_user_details(db: Session, id: int, details:to_do.schemas.UpdateUser):
    db.query(to_do.models.User).filter(to_do.models.User.id == id).update(vars(details))
    db.commit()
    return db.query(to_do.models.User).filter(to_do.models.User.id == id).first()


def delete_user(db: Session, user_id: int):
    """ 
    Delete user from databse. An exception will be raised if
    an invalid ID is provided.

    """

    try:
        db.query(to_do.models.User).filter(to_do.models.User.id == user_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)


def create_user_task(db: Session, task: to_do.schemas.TaskCreate, user_id: int):
    db_todo = to_do.models.Tasks(**task.dict(), owner_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def create_task(db: Session, todo: to_do.schemas.TaskCreate):
    db_todo = to_do.models.Tasks(content=todo.content)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


# This function will get all Tasks
def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(to_do.models.Tasks).offset(skip).limit(limit).all()


# This function will get a task by ID 
def get_todo_by_id(db: Session, user_id: int):
    return db.query(to_do.models.Tasks).filter(to_do.models.Tasks.id == user_id).first()


# This function will update a task
def update_task_details(db: Session, id: int, details:to_do.schemas.UpdateUserTask):
    db.query(to_do.models.Tasks).filter(to_do.models.Tasks.id == id).update(vars(details))
    db.commit()
    return db.query(to_do.models.Tasks).filter(to_do.models.Tasks.id == id).first()

# This function will delete a task
def delete_task(db: Session, task_id: int):
    try:
        db.query(to_do.models.Tasks).filter(to_do.models.Tasks.id == task_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)    


def update_task(db: Session, id: int, details:to_do.schemas.UpdateTask):
    db.query(to_do.models.Tasks).filter(to_do.models.Tasks.id == id).update(vars(details))
    db.commit()
    return db.query(to_do.models.Tasks).filter(to_do.models.Tasks.id == id).first()
   
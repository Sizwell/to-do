from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    surname: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    name: str
    surname: str

    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    name: str
    surname: str  

    class config:
        orm_mode = True 


class TaskBase(BaseModel):
    content: str
    done: bool


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int 
    content: str
    done: bool

    class config:
        orm_mode = True 


class UpdateUserTask(BaseModel):
    content: str
    done: bool 

    class config:
        orm_mode = True      


class UpdateTask(BaseModel):
    owner_id: int
    done: bool

    class config:
        orm_mode = True 

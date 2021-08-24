from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from to_do.db import Base


UserTasks = Table(
    'usertasks', Base.metadata,
    Column('user_id', Integer, ForeignKey("users.id")),
    Column('task_id', Integer, ForeignKey("tasks.id")) 
)  


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)

    tasks = relationship("Tasks", secondary=UserTasks, back_populates='owner')

    def __repr__(self):
        return f"<Name={self.name} Surname={self.surname}>"


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    done = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", secondary=UserTasks, back_populates='tasks')

    def __repr__(self):
        return f"<Content={self.content} Done={self.done}  Owner id={self.owner_id}>"

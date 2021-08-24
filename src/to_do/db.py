import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from dotenv import load_dotenv
load_dotenv()

driver = os.environ['DRIVER']
username = os.environ['USERNAME']
password= os.environ['PASSWORD']
serverName = os.environ['SERVERNAME']
port = os.environ['PORT']
database = os.environ['DATABASE']
host = os.environ['HOST']

engine = create_engine(
    f"{driver}://{username}:{password}@{host}:{port}/{database}", 
    echo=True
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

Base.metadata.create_all(engine)

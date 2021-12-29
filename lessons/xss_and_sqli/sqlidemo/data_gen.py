import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()

engine = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
Base.metadata.bind = engine
db_session = sessionmaker(bind=engine)
session = db_session()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=128), unique=True, nullable=False)
    password = Column(String(length=128), nullable=False)
    admin = Column(Boolean)
    
try:
    Base.metadata.create_all(engine)
except Exception as e:
    print(e)
    
users = [User(name='user-1', password='password', admin=False),
         User(name='user-2', password='password2', admin=False),
         User(name='user-3', password='password3', admin=False),
         User(name='user-4', password='password3', admin=True)]
for user in users:
    session.add(user)
session.commit()
session.close()
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
    
def is_admin(username: str) -> bool:
    object: User = session.query(User).filter(User.name==username).first()
    if object is None:
        return False
    return object.admin

print(is_admin('user-4'))
print(is_admin("'; select true; --"))
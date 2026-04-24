from database import Base
from sqlalchemy import Column, Integer, String

class Iphone(Base):
   __tablename__ = "iphones"

   id = Column(Integer, primary_key=True, index=True)
   version = Column(String)
   serialNumber = Column(String)
   userID = Column(String, unique=True, index=True)
   userName = Column(String)
   phoneNumber = Column(String)
   birthDay = Column(String)

class Deleted_iphone(Base):
   __tablename__ = "deleted_iphones"

   id = Column(Integer, primary_key=True, index=True)
   userID = Column(Integer, unique=True, index=True)
   serialNumber = Column(String, unique=True)

class Workers(Base):
   __tablename__ = "workers"

   id = Column(Integer, primary_key=True, index=True)
   workerID = Column(Integer, unique=True, index=True)
   country = Column(String)
   age = Column(Integer)
   salary = Column(String)
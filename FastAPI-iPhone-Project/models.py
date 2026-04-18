from pydantic import BaseModel

class Iphone(BaseModel):
   version: int
   serialNumber: int
   userID: int
   userName: str
   phoneNumber: int
   birthDay: int
   


class Deleted_iphone(BaseModel):
    userID: int
    userName: str

class Workers(BaseModel):
    workerID: int
    country: str
    age: int
    salary: str

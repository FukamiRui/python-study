from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine, get_db, get_connection
import models
from models import Iphone, Deleted_iphone, Workers

from sqlalchemy.orm import Session
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
   CORSMiddleware,
   allow_origins = ["*"],
   allow_methods = ["*"],
   allow_headers = ["*"]
)
# The CORSMiddleware makes accessable 

# main.py
print("--- DB Debug Start ---")
print(f"Registered tables: {Base.metadata.tables.keys()}") 
Base.metadata.create_all(bind=engine)
print("--- DB Debug End ---")

Base.metadata.create_all(bind = engine)


class IphoneCreate(BaseModel):
   version: int
   serialNumber: int
   userID: int
   userName: str
   phoneNumber: int
   birthDay: int
   


class Deleted_iphoneCreate(BaseModel):
    userID: int
    serialNumber: str

class WorkersCreate(BaseModel):
    workerID: int
    country: str
    age: int
    salary: str



#1. Here is for users data

@app.post("/iphone")
async def create_iphone(iphone: IphoneCreate, db: Session = Depends(get_db)):
   new_iphone = models.Iphone(
      version= iphone.version,
      serialNumber=iphone.serialNumber,
      userID=iphone.userID,
      phoneNumber=iphone.phoneNumber,
      birthDay=iphone.birthDay
   )
   db.add(new_iphone)
   db.commit()
   db.refresh(new_iphone)
  

   return {
      "message": f"successfully this iphone {new_iphone.id} is successfully added to the Database"
      }


@app.get("/iphone/{userID}")
async def get_iphone(userID: str, db: Session=Depends(get_db)):
   iphone = db.query(models.Iphone).filter(models.Iphone.userID == userID).first()
   
   if iphone is None: 
      raise HTTPException(status_code=404, detail="The ID is not found, please try again.")
   
   return iphone  
   
        


#Before delete the specific data from the database, store the datas just in case.
@app.delete("/iphone/{userID}")
async def delete_iphone(userID: str, db: Session=Depends(get_db)):
  iphone = db.query(models.Iphone).filter(models.Iphone.userID == userID).first()

  if iphone is None:
      raise HTTPException(status_code=404, detail="The iphone ID is not found")
  else:
      {"message": "Your deleted id and serial number will be saved on the database."}

  backup_data = models.Deleted_iphone(
                                     userID = iphone.userID,
                                     serialNumber = iphone.serialNumber
                                     
                                     )

  db.add(backup_data)
  db.delete(iphone)
  db.commit()

  return {"message": f"The ID: {userID} will be deleted"}



@app.put("/iphone/{userID}")
async def update_iphone_info(userID: int, update_data: IphoneCreate, db: Session = Depends(get_db)):

   update_iphone = db.query(models.Iphone).filter(models.Iphone.userID == userID).first()
   

   if update_iphone is None:
      raise HTTPException(status_code=404, detail="The iphone is not found")
   else:
      {"message": "No longer you can't access your current account info."}
   
   update_iphone.version = str(update_data.version)
   update_iphone.serialNumber = str(update_data.serialNumber)
   update_iphone.userName = str(update_data.userName)
   update_iphone.phoneNumber = str(update_data.phoneNumber)
   update_iphone.birthDay = str(update_data.birthDay)
   update_iphone.userID = str(update_data.userID)

   db.commit()

   return{"message": f"Hi {update_iphone.userName}, Your UserID has been changed to {userID}"}

      
# ALL returns have to be dictionary {} for JSON 
    
#2 for deleted user's information database

@app.post("/deleted_iphone")
async def create_lists(deleted_iphone: Deleted_iphoneCreate, db: Session = Depends(get_db) ):
    new_deleted_iphone = models.Deleted_iphone(
                     userID = deleted_iphone.userID,
                     userName = deleted_iphone.serialNumber
                     )
    db.add(new_deleted_iphone)
    db.commit()
    db.refresh(new_deleted_iphone)
   




#3  for labors informatiton database
@app.post("/workers")
async def create_worker(worker: WorkersCreate, db: Session = Depends(get_db)):
   new_worker = models.Workers(
                              workerID = worker.workerID,
                              country = worker.country,
                              age = worker.age,
                              salary = worker.salary
                             )
   
   db.add(new_worker)
   db.commit()
   db.refresh(new_worker)

   return {"message": f"Hello, welcome to $$Company. Now your information is successfully added. Your ID is {new_worker.workerID}"}

@app.get("/workers/{workerID}")
async def get_workerID(workerID: int, db: Session = Depends(get_db)):

  woker = db.query(models.Workers).filter(models.Workers.workerID == workerID).first()

  if woker is None:
     raise HTTPException(status_code=404, detail="The ID is not found")
  
  return woker
  


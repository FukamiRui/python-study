from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Iphone, Deleted_iphone, Workers
from database import get_connection, init_database




# The CORSMiddleware makes accessable 

app = FastAPI()

init_database()

app.add_middleware(
   CORSMiddleware,
   allow_origins = ["*"],
   allow_methods = ["*"],
   allow_header = ["*"]
)

#1. Here is for users data

@app.post("/iphone")
async def create_iphone(iphone: Iphone):
   connect = get_connection()
   cursor = connect.cursor()

   cursor.execute("INSERT INTO iphones (version, serialNumber, userID, userName, phoneNumber, birthDay) VALUES(?,?,?,?,?,?)",
   (iphone.version, iphone.serialNumber, iphone.userID, iphone.userName, iphone.phoneNumber, iphone.birthDay))

   new_id = cursor.lastrowid 
   connect.commit()
   connect.close()

   return {
      "message": f"successfully this iphone {new_id} is successfully added to the Database"
      }


@app.get("/iphone/{userID}")
async def get_iphone(userID: int):
   connect = get_connection()
   cursor = connect.cursor()

   cursor.execute("SELECT * FROM iphones WHERE userID = ?", (userID,))
   row = cursor.fetchone()
   connect.close()

   if row:
      return {  "version": row["version"], "serialNum": row["serialNumber"], "userID": row["userID"], "userName": row["userName"], "phoneNumber": row["phoneNumber"], "birthDay": row["birthDay"]}
   else: 
      connect.close()
      raise HTTPException(status_code=404, detail="The ID is not found, please try again.")
      
   
        


#Before delete the specific data from the database, store the datas just in case.
@app.delete("/iphone/{userID}")
async def delete_iphone(userID: int):
   connect = get_connection()
   cursor = connect.cursor()
   cursor.execute("SELECT * FROM iphones WHERE userID = ?", (userID,))
   row = cursor.fetchone()

   if row is None:
      connect.close()
      raise HTTPException(status_code=404, detail="The iphone ID is not found")
   else: 
      cursor.execute("INSERT INTO deleted_iphone(userID, userName) VALUES(?,?)",
                     (row["userID"], row["userName"]))
      
      cursor.execute("DELETE FROM iphones WHERE userID = ?", (userID,))
      connect.commit()
      connect.close()
      return {"message": f"The ID: {userID} will be deleted"}



@app.put("/iphone/{userID}")
async def update_iphone_info(userID: int, update_iphone_info: Iphone):
   connect = get_connection()
   cursor = connect.cursor()
  
   oldID = userID

   cursor.execute("SELECT * FROM iphones WHERE userID = ?", (userID,)) 
   row = cursor.fetchone()

   if row is None:
      connect.close()
      raise HTTPException(status_code=404, detail="The ID is not found")
   
   cursor.execute('''
                 UPDATE iphones
                  SET version = ?, serialNumber = ?, userName = ?, phoneNumber = ?, birthDay = ?
                  WHERE userID = ? ''',
                  (update_iphone_info.version, 
                   update_iphone_info.serialNumber, 
                   update_iphone_info.userName,
                   update_iphone_info.phoneNumber,
                   update_iphone_info.birthDay,
                   update_iphone_info.userID
                   ))
   connect.commit()
   connect.close()

   return {"message": f"The {oldID} has been updated to: {update_iphone_info.userID} "}


      
# ALL returns have to be dictionary {} for JSON 
    
#2 for deleted user's information database

@app.post("/deleted_iphone")
async def create_lists(deleted_iphone: Deleted_iphone):
    connect = get_connection()
    cursor = connect.cursor()

    cursor.execute("INSERT INTO deleted_iphone(userID, userName) VALUES(?,?)",
                   (deleted_iphone.userID, deleted_iphone.userName))
    connect.commit()
    connect.close()

    return {"message": f"The deleted user table is created on the database"}




#3  for labors informatiton database
@app.post("/workers")
async def create_worker(worker: Workers):
   connect = get_connection()
   cursor = connect.cursor()
   
   cursor.execute("INSERT INTO workers (workerID, country, age, salary) VALUES(?,?,?,?)",
                  (worker.workerID, worker.country, worker.age, worker.salary ))

    
   new_ID = cursor.lastrowid
   connect.commit()
   connect.close()

   return {"message": f"Hello, welcome to $$Company. Now your information is successfully added. Your ID is {new_ID}"}

@app.get("/workers")
async def get_workerID(workerID: int):
   connect = get_connection()
   cursor = connect.cursor()
   cursor.execute("SELECT * FROM workers WHERE workerID = ?", (workerID,))
   row = cursor.fetchone()
   connect.close()

   if row is None:
      raise HTTPException(status_code=404, detail="This workerID is not registered. Try again.")

   return {"message": f"This workerID is {workerID} "}

    
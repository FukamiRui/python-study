from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# The CORSMiddleware makes accessable 

app = FastAPI()

app.add_middleware(
   CORSMiddleware,
   allow_origins = ["*"],
   allow_methods = ["*"],
   allow_header = ["*"]
)

class Iphone(BaseModel):
   version: int
   price: int

db_iphone = {}

@app.post("/iphone")
async def create_iphone(iphone: Iphone):
   serialNum = len(db_iphone) + 1
   db_iphone[serialNum] = iphone

   return {
      "message": f"successfully this iphone {serialNum} is posted",
      "version": iphone.version,
      "price": f"{iphone.price} USD"
      }

@app.get("/iphone/{serialNum}")
async def get_iphone(serialNum: int):
   if serialNum in db_iphone:
      return db_iphone[serialNum]
   else:
      return {"message": "The iphone is not found"}

@app.get("/iphones/")  
async def get_all_iphone():
      return db_iphone

#Before delete the specific data from the database, store the datas just in case.
@app.delete("/iphone/{serialNum}")
async def delete_iphone(serialNum: int):
   if serialNum in db_iphone:
      info = db_iphone[serialNum]
      del db_iphone[serialNum]
      return {f"The {info.version} and{info.price} is deleted"}
   return {"ERROR": "The iphone is not found"}



@app.put("/iphone/{serialNum}")
async def update_iphone_info(serialNum: int, update_iphone_info: Iphone):
   if serialNum not in db_iphone:
      return {f"The iphone {serialNum} is not found"}
   
   db_iphone[serialNum] = update_iphone_info
   return {f"The updated serial number is {serialNum}"}
      
# ALL returns have to be dictionary {} for JSON 
    
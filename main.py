from fastapi import FastAPI,Depends,HTTPException,status
import requests
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager
import pandas as pd
from db.models import Cities, WeatherStorage
from typing import List, Annotated
from datetime import datetime
from db.schemas import Add_Cities
from pydantic import BaseModel
from db.database import init_db
from db.database import get_session
from service import CityService

cit_service=CityService()

@asynccontextmanager
async def life_span(app:FastAPI):
    print("server starting")
    init_db()
    yield
    print("server ending")

app = FastAPI(lifespan=life_span)
@app.get('/')
def read_root():
    return {"message":"db init finally"}


@app.post('/',status_code=status.HTTP_201_CREATED,response_model=Cities)
def create_entry(city_data:Add_Cities,session:Session = Depends(get_session))->dict:
    new_entry=cit_service.add_city(city_data,session)
    return new_entry

#weather api to add it 



    

#api_key='e34128606d6448b88c6150147252905'
#location=input("Enter your location in city form : ")
#url=f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no"
#df=pd.read_json(url)
#rint(df)


#df.to_sql('empl')
#weather=requests.get(url).json()
#print(weather)
#data = {
 #   f"City:{weather['location']['name']}\n"\
   # f"Country:{weather['location']['region']}\n"\
   #f"Temperature:{weather['current']['temp_c']}\n"\
#}
#print(data)

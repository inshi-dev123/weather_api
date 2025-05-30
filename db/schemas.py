from pydantic import BaseModel
from datetime import datetime
from uuid import UUID



class city(BaseModel):
    city_id:UUID #this will be base primary key for each city
    city_location:str
    country:str
    lat:float
    long:float



class Add_Cities(BaseModel):
    city_location:str

class Weath_storage(BaseModel):
    city_loc:str
    localtime:datetime
    temp_c:float

 
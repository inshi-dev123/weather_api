from db.schemas import Add_Cities
from db.database import Session
import requests
from sqlmodel import select, Session
from db.models import Cities
api_key='e34128606d6448b88c6150147252905'

class CityService:

    def get_all_cities(self, session:Session):
        statement=select(Cities)
        result = session.exec(statement)
        return result.all()
    
   
    def get_city(self,city_loc:str,session:Session):
        statement=select(Cities).where(Cities.city_location==city_loc )
        result = session.exec(statement)
        return result.first()
    

    def add_city(self,city_data:str,session:Session):
        url=f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_data}&aqi=no"
        # need to put check here to see if its not present in database alredy
        weather=requests.get(url).json()
        new_record=Cities()
        new_record.city_location=weather['location']['name']
        new_record.country=weather['location']['country']
        new_record.long=weather['location']['lon']
        new_record.lat=weather['location']['lat']
        session.add(new_record)
        session.commit()
        return new_record
    

    def delete_city(self,city_name:str,session:Session):
        city_delete = self.get_city(city_name,session)
        if city_delete is not None:
            session.delete(city_delete)
            session.commit()
        else :
            return None

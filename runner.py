from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
import uuid
import sqlalchemy.dialects.postgresql as pg
from sqlalchemy import Column
from db.schemas import Add_Cities
from service import Weath_Service
from db.database import Session
import requests
import datetime
from main import Session
from sqlmodel import select, Session
from db.models import Cities, WeatherStorage 
from db.database import SessionLocal

object= Weath_Service()

with SessionLocal() as session:
    object.add_Entries(session)



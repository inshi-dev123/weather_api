from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
import uuid
import sqlalchemy.dialects.postgresql as pg
from sqlalchemy import Column

class Cities(SQLModel, table=True):
    __tablename__ = 'cities'
    
    city_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(
            pg.UUID(as_uuid=True),
            primary_key=True,
            index=True
        )
    )
    city_location: str
    country: str
    lat: float
    long: float

class WeatherStorage(SQLModel, table=True):
    city_id: uuid.UUID = Field(foreign_key="cities.city_id", primary_key=True)
    updated_at: datetime = Field(default_factory=datetime.utcnow, primary_key=True)
    city_location: str
    temp_c: float


    __table_args__ = (
        {'primary_key': ['city_id', 'updated_at']},
    )
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.orm import sessionmaker
from db.models import WeatherStorage, Cities
DATABASE_URL = 'postgresql://neondb_owner:npg_BDkzUg0T1sQa@ep-bold-surf-a8olvf5d-pooler.eastus2.azure.neon.tech/neondb?sslmode=require'

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    print("init db")
    SQLModel.metadata.create_all(bind=engine)
    print("table created")

SessionLocal = sessionmaker(bind=engine,class_=Session)

def get_session():
   db= SessionLocal()
   yield db
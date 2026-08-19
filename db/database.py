from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "mysql+mysqlconnector://root:password@localhost:3306/telusko"
engine = create_engine(db_url)
session = sessionmaker(autoflush=False,autocommit=False,bind=engine)

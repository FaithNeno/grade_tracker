from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
#this string  tells SQLAlchemy exactly where our database lives (./ - means 'in this same folder)
DATABASE_URL = "sqlite:///./grades.db"
 
#The engine is the actual connection to the database.
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
 
#SessionLocal - is a blueprint for creating sessions
#autocommit=False - we control when data is saved
#autoflush=False - SQLAlchemy will NOT automatically send changes to the database
#bind=engine - Tells SessionLocal which engine(which database connection)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


#Base is a parent class for all our database models.
#class Student(Base)- SQLAlchemy will know Student is database table.
Base = declarative_base()


def get_db(): # regular function
    db = SessionLocal() # creates a fresh database session
    try:    # start block where we do the work
        yield db # gives the session to whoever called get_db and PAUSE
    finally:    # this block runs no matter what(whether the request succeeded or failed)
        db.close()  # close the seesion
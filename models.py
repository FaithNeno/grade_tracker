# Column is how we define a column in our table 
# Integer, String, Float - are the data types for each column
from sqlalchemy import Column, Integer, String, Float 
# we import Base from our file (database.py) 
# Base - parent class our Student will inherit from
from database import Base 

class Student(Base):    # Python class called Student 
    __tablename__ = "students"  # this sets the actual name of the table inside the database

    id = Column(Integer, primary_key=True, index=True) # unique identifier 
    name = Column(String, nullable=False) # string is a text , nullable=False - means the field is required
    course = Column(String, nullable=False)
    grade = Column(Float, default=0.0) # if no grade given it will default to 0.0 
    email = Column(String, unique=True) # unique=True - means no two students can have same email address 
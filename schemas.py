
# pydantic is the validation library 
# BaseModel is the parent class for all our schemas. (same idea as Base In SQLALchemy )
from pydantic import BaseModel

# Optional lets us mark fields as not required. (we nedd this is for any UPDATE schema)
from typing import Optional

# StudentCreate - what the user sends to CREATE 
# -is the schema for when someone wants to ADD a new student. 
# (These are the field they must send in ther request)
class StudentCreate(BaseModel):
    name: str # name is require and must be a string 
    course: str 
    grade: float = 0.0 # grade is optional, if not sent , it defaults to 0.0 
    email: str 


# StudentUpdate - what the user sends to UPDATE 
# Is the schema for when someone wnats to change a student's detail. 
# Optional because when updating a user should able to send just one field and change only that
class StudentUpdate(BaseModel):
    name: Optional[str] = None # name is optional. If not sent, it is None (and we will skip updating it)
    course: Optional[str] = None 
    grade: Optional[float] = None 


# StudentResponse -  what the API sends BACK 
# id - because after we create a student, we want to tell the user what id they were assigned. 
class StudentResponse(BaseModel):
    id: int 
    name: str 
    course: str 
    grade: float
    email:str 

    class Config:   # special inner class 
        from_attributes = True # without this line. Pydantic cannot real SQLAlchemy model objects
                                # this line will tell it, also accept SQLAlchemy objects

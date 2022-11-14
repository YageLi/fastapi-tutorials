from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str

class Show_Blog(Blog):
    # or just do this, then it will be just showing title property
    # title: str
    class Config:
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str

class Show_User(BaseModel):
    name:str
    email:str
    class Config:
        orm_mode = True
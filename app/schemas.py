from wsgiref.validate import validator
from pydantic import BaseModel, EmailStr

class UserRegistration(BaseModel):
    email: EmailStr
    password: str


# Request body model for update
class UpdateNoteRequest(BaseModel):
    title: str
    content: str
    
class UserOut(BaseModel):
    user_id: str
    user_name: str
    user_email: EmailStr
    mobile_number: str
    created_on: str

class UserAuth(BaseModel):
    user_email: EmailStr
    password: str

class NoteCreate(BaseModel):
    note_title: str
    note_content: str

class NoteOut(BaseModel):
    note_id: str
    note_title: str
    note_content: str
    created_on: str
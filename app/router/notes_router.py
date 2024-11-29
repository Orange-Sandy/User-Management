from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import decodeJWT
from app.schemas import UpdateNoteRequest
from fastapi import APIRouter, HTTPException, Depends
from bson import ObjectId
from app.database.main.mongo import notes_collection

router = APIRouter()


@router.post("/notes", dependencies=[Depends(JWTBearer())], tags=["Create Note"])
async def create_note(title: str, content: str, token: str = Depends(JWTBearer())):
    user = decodeJWT(token)
    print(user)
    note = {
        "user_id": user["user_id"],
        "title": title,
        "content": content
    }
    notes_collection.insert_one(note)
    return {"message": "Note created successfully"}

@router.get("/notes", dependencies=[Depends(JWTBearer())], tags=["View Notes"])
async def view_notes(token: str = Depends(JWTBearer())):
    user = decodeJWT(token)
    # Fetch notes for the user
    notes_cursor = notes_collection.find({"user_id": user["user_id"]})
    notes = [convert_objectid_to_str(note) for note in notes_cursor.to_list(length=100)]
    return notes

@router.put("/notes/{note_id}", dependencies=[Depends(JWTBearer())], tags=["Update Note"])
async def update_note(note_id: str, request: UpdateNoteRequest, token: str = Depends(JWTBearer())):
    user = decodeJWT(token)  # Assuming decodeJWT decodes the JWT token and returns the user information

    # Convert note_id from string to ObjectId
    try:
        note_id_obj = ObjectId(note_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid note_id format.")

    # Find the note by note_id and user_id
    note = notes_collection.find_one({"_id": note_id_obj, "user_id": user["user_id"]})
    if not note:
        raise HTTPException(status_code=404, detail="Note not found or not owned by user.")
    
    # Update the note in the database
    notes_collection.update_one(
        {"_id": note_id_obj},
        {"$set": {"title": request.title, "content": request.content}}
    )
    return {"message": "Note updated successfully"}

@router.delete("/notes/{note_id}", dependencies=[Depends(JWTBearer())], tags=["Delete Note"])
async def delete_note(note_id: str, token: str = Depends(JWTBearer())):
    # Convert note_id from string to ObjectId
    try:
        note_id_obj = ObjectId(note_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid note_id format.")
    user = decodeJWT(token)
    note = notes_collection.find_one({"_id": note_id_obj, "user_id": user["user_id"]})
    if not note:
        raise HTTPException(status_code=404, detail="Note not found or not owned by user.")
    
    notes_collection.delete_one({"_id": note_id_obj})
    return {"message": "Note deleted successfully"}


# Helper function to convert ObjectId to string
def convert_objectid_to_str(note):
    if '_id' in note and isinstance(note['_id'], ObjectId):
        note['_id'] = str(note['_id'])
    return note




import uuid
from datetime import datetime, timezone

def user_model():
    return {
        "user_id": str(uuid.uuid4()),
        "user_name": "",
        "user_email": "",
        "mobile_number": "",
        "password": "",
        "last_update": datetime.now(timezone.utc),
        "created_on": datetime.now(timezone.utc),
    }

def note_model():
    return {
        "note_id": str(uuid.uuid4()),
        "note_title": "",
        "note_content": "",
        "last_update": datetime.now(timezone.utc),
        "created_on": datetime.now(timezone.utc),
    }

from http.client import HTTPException

from app.auth import hash_password
from app.models import user_model


@router.post("/register", response_model=UserOut)
async def register_user(user: UserCreate, db: AsyncIOMotorDatabase = Depends(get_db)):
    """
    Register a new user. Password is hashed, and email must be unique.
    """
    users_collection = db.get_collection("users")
    
    # Check if email already exists
    existing_user = await users_collection.find_one({"user_email": user.user_email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered.")
    
    # Hash the password
    hashed_pwd = hash_password(user.password)
    
    # Prepare user data
    new_user = user_model()
    new_user.update(user.dict())
    new_user["password"] = hashed_pwd  # Replace plain password with hashed password
    
    # Insert the user into the database
    await users_collection.insert_one(new_user)
    return new_user

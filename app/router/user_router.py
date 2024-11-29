from app.auth.auth_handler import signJWT
from app.schemas import UserRegistration
from fastapi import HTTPException, APIRouter
from app.database.main.mongo import users_collection
from app.config import settings
from passlib.context import CryptContext

router = APIRouter()

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

async def check_email_exists(email: str) -> bool:
    user = users_collection.find_one({"email": email})
    return user is not None

@router.post("/register", tags=["User Registration"])
async def register_user(user: UserRegistration):
    if await check_email_exists(user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = hash_password(user.password)
    user = {
        "email": user.email,
        "password": hashed_password,
    }
    users_collection.insert_one(user)
    return {"message": "User registered successfully"}

# User login and JWT generation
@router.post("/login", tags=["User Login"])
async def user_login(email: str, password: str):
    user = users_collection.find_one({"email": email})
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Generate JWT Token
    return signJWT(str(user["_id"]))

@router.post("/logout", tags=["User Logout"])
async def user_logout():
    return {"message": "Successfully logged out. Please remove the tokens on the client-side."}

from fastapi import FastAPI, HTTPException, Request
from app.router.user_router import router as Users
from app.router.notes_router import router as Notes
# from app.router.auth_router import router as Auth

app = FastAPI(title="Notes Management")

app.include_router(Users, prefix="/users")
app.include_router(Notes, prefix="/notes")


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host = '127.0.0.1',port = 8009)
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import jwt
from datetime import datetime, timezone, timedelta
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

SECRET_KEY = "3495project1"
app = FastAPI()

# Set up templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

users_db = {"asdf": "123"}

class LoginRequest(BaseModel):
    username: str
    password: str

def create_jwt(username: str):
    payload = {
        "sub": username,
        "exp": datetime.now(timezone.utc) + timedelta(hours=1),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

@app.get("/", response_class=HTMLResponse)
def serve_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/")
def login(data: LoginRequest):
    if users_db.get(data.username) == data.password:
        token = create_jwt(data.username)
        return {"access_token": token} 
    raise HTTPException(status_code=401, detail="Invalid credentials")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)

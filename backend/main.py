from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import create_db_connection
from .models import User

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/users')
def get_users():
    db_connection = create_db_connection()
    users = db_connection.query(User).all()
    db_connection.close()
    return users

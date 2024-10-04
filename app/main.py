from fastapi import FastAPI
from app.api import auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Reemplaza con la URL de tu app Next.js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/data")
def get_data():
    return {"message": "Hello from FastAPI", "data": [1, 2, 3, 4, 5]}

app.include_router(auth_router.router)
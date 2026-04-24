"""
Arranca la API FastAPI (uvicorn).rando e

  python main.py

Documentación interactiva: http://127.0.0.1:8000/docs

Para crear tablas en la base de datos, usa: python init_db.py
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:4200",
    "https://sistema-reservas-flax.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # o ["*"] para probar
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

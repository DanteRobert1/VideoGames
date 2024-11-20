from fastapi import FastAPI
from game import game

app = FastAPI()

@app.get("/")
def home():
    return "Dame tus Juegos jeje"

@app.get("/name/{name}")
def greeting(name:str):
    return "Hola"+ name

app.include_router(game)

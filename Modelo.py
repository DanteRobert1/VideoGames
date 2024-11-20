from pydantic import BaseModel

class Videojuego(BaseModel):
    titulo: str  
    genero: str 
    plataforma: str  

class Caracteristicas(BaseModel):
    id: int  
    videojuego: Videojuego  
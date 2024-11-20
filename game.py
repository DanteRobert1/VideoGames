from fastapi import APIRouter,Path
from Modelo import Caracteristicas

game_list:Caracteristicas = []

game = APIRouter()

@game.post("/game")
def add_game(game:Caracteristicas):
    game_list.append(game)
    return{"message": "Added"}


@game.get("/game")
def show_games():
       return {"games": game_list}


@game.get("/game/{game_id}")
def show_one_game(game_id:int=Path(...,title="ID")):
      for game in game_list:
            if game.id == game_id:
                return{"game":game}
      return {"message": "ID doesn't exist"}
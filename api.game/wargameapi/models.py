from typing import NamedTuple

class Player(NamedTuple):
    name: str
    deck: list
    hand: list

class GameState(NamedTuple):
    playerOne: Player
    playerTwo: Player
    gameID: str
    handHistory: list

class PlayedGame(NamedTuple):
    gameID: str
    winner: str
    players: list
    handsHistory: list
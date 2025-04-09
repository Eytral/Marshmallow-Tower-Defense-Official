GAME_DATA = {
    "Easy": {
        "Game_Stats": {
            "Starting Money": 75,
            "Starting Health": 120
        },
        "Default_Spawn": {
            "marshmallow enemy": 3,
            "cracker enemy": 1,
            "white_chocolate enemy": 0,
            "dark_chocolate enemy": 0,
            "smore enemy": 0
        },
        "Increment": {
            "marshmallow enemy": 3,
            "cracker enemy": 1.5,
            "white_chocolate enemy": 1,
            "dark_chocolate enemy": 0.5,
            "smore enemy": 0.2
        },
        "Default_Spawn_Interval": 60,
        "Last Wave": 20
    },

    "Normal": {
        "Game_Stats": {
            "Starting Money": 75,
            "Starting Health": 80
        },
        "Default_Spawn": {
            "marshmallow enemy": 4,
            "cracker enemy": 1,
            "white_chocolate enemy": 0,
            "dark_chocolate enemy": 0,
            "smore enemy": 0
        },
        "Increment": {
            "marshmallow enemy": 4,
            "cracker enemy": 2,
            "white_chocolate enemy": 1.5,
            "dark_chocolate enemy": 0.75,
            "smore enemy": 0.3
        },
        "Default_Spawn_Interval": 50,
        "Last Wave": 30
    },

    "Hard": {
        "Game_Stats": {
            "Starting Money": 75,
            "Starting Health": 40
        },
        "Default_Spawn": {
            "marshmallow enemy": 6,
            "cracker enemy": 3,
            "white_chocolate enemy": 1,
            "dark_chocolate enemy": 0,
            "smore enemy": 0
        },
        "Increment": {
            "marshmallow enemy": 5,
            "cracker enemy": 3,
            "white_chocolate enemy": 2,
            "dark_chocolate enemy": 1,
            "smore enemy": 0.4
        },
        "Default_Spawn_Interval": 40,
        "Last Wave": 35
    },
}

from Entities.Enemies.marshmallow_enemy import Marshmallow
from Entities.Enemies.cracker_enemy import Cracker
from Entities.Enemies.white_chocolate_enemy import WhiteChocolate
from Entities.Enemies.dark_chocolate_enemy import DarkChocolate
from Entities.Enemies.smore_enemy import Smore

ENEMY_CLASS_MAP = {
    "marshmallow enemy": Marshmallow,
    "cracker enemy": Cracker,
    "white_chocolate enemy": WhiteChocolate,
    "dark_chocolate enemy": DarkChocolate,
    "smore enemy": Smore,
}
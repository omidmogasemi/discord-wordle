import enum 

class GameStatus(enum.Enum): 
    DEAD = 0 
    JOINING = 1 
    PLAYING = 2 
    DONE = 3 
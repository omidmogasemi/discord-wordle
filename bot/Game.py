from typing import Final
import uuid 
from Word import Word 
from Tip import Tip 
from GameStatus import GameStatus 
from PlayerStatus import PlayerStatus 

"""A representation of a singular game. 

    Attributes:
        id: A UUID representing the current game. 
        owner: The Discord UUID of the game creator and owner. 
        status: The current state of the game. 
        players: A dictionary of {playerID: (numberOfTurnsUsed, hasFinished)} values. 
        word: The current word being guessed. 
""" 

class Game: 
    MAX_GUESSES: Final = 6 

    def __init__(self, owner): 
        """Inits Game class with specified owner UUID.""" 
        self.id = uuid.uuid4() 
        self.owner = owner 
        self.status = GameStatus.JOINING  
        self.players = {owner: PlayerStatus.ZERO} 
        self.word = Word() 

    def join(self, player): 
        """Adds a player to the game. 

        Args:
            player: Discord UUID of the user attempting to join. 

        Returns:
            True if the user was able to join the game. 
            False otherwise. 
        """ 
        if player != self.owner and player not in self.players and self.status == GameStatus.JOINING: 
            self.players[player] = (0, False) 
            return True 
        
        return False 
    
    def start(self): 
        """Starts the current game.""" 
        if self.status != GameStatus.JOINING: # TO-DO: Make this throw an exception 
            return None 
        
        self.status = GameStatus.PLAYING 
    
    def guess(self, guesser, word): 
        """Checks if a guess was correct, updating the players dict accordingly. 

        Args: 
            guesser: The UUID of the user guessing. 
            word: The word the user is guessing. 
        
        Returns: 
            (True/False, guess_response) 
            True if the user guessed correctly, False if the user guessed incorrectly. 

            guess_response is a 6-value list containing the correctness of each guess. 
        """ 

        if guesser not in self.players or self.players[guesser] == PlayerStatus.SIX or self.players[guesser] == PlayerStatus.SUCCESS: 
            return False # TO-DO: Make this throw an exception 
        
        status, result = self.word.calc_accuracy(word) 
        self.players[guesser] = PlayerStatus(self.players[guesser].value + 1) if not status else PlayerStatus.SUCCESS 

        return status, result 
    
    def end(self, player): 
        """Ends a currently running game.""" 
        if player == self.owner and self.status == GameStatus.PLAYING: 
            self.status = GameStatus.DONE 
            return True 
        
        return False 
        
g = Game(123) 
print(g.guess(124, "blahhh")) 
print(g.guess(123, "test")) 
print(g.players) 
print(g.guess(123, "test")) 
print(g.players) 
print(g.guess(123, "adieu")) 
print(g.players) 
print(g.guess(123, "adieu")) 

from typing import Final 
from Word import Word 
from Tip import Tip 

class Game: 
    MAX_GUESSES: Final = 6 

    def __init__(self, id, name): 
        self.id = id 
        self.name = name 
        self.gameActive = False 
        self.player = None 
        self.guesses = 0 
        self.w = Word() 
    
    def isActive(self): 
        return self.gameActive 
    
    def startGame(self, player): 
        if not self.gameActive: 
            self.gameActive = True 
            self.player = player 
            self.w.setWord("Adieu") 
            return True, self.player 
        else: 
            return False, None 
    
    def endGame(self, player): 
        if self.player != player: 
            return False 
        
        if not self.gameActive: 
            return False 
        
        self.player = None 
        self.gameActive = False 
        return True 
    
    def guess(self, guess, player): 
        if player != self.player: 
            return False, None 

        if self.guesses >= self.MAX_GUESSES or not self.gameActive: 
            self.endGame(player) 
            return False, None 
        
        correct, res = self.w.calcAccuracy(guess) 
        if correct: 
            self.endGame(player) 
        else: 
            self.guesses += 1 

        return correct, res 
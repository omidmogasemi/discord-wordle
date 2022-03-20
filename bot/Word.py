from Tip import Tip 

"""A representation of a singular word. 

    Attributes:
        word: The current word being operated on. 
""" 

class Word: 
    def __init__(self): 
        self.word = "ADIEU" 
        # TO-DO: Implement an algorithm to automatically create the word 
    
    def calc_accuracy(self, guess): 
        """Calculates if a guess was correct. 

        Determines a detailed list of if each letter was in the correct spot, 
        in the wrong spot, or does not exist in the word at all. 

        Attributes:
            guess: The user's current word choice being examined. 
        """ 
        
        guess = guess.upper() 
        res = [] 
        for i, j in zip(guess, self.word): 
            if i == j: 
                res.append(Tip.CORRECT) 
            elif i in self.word: 
                res.append(Tip.PRESENT) 
            else: 
                res.append(Tip.ABSENT) 

        return (True, res) if Tip.PRESENT not in res and Tip.ABSENT not in res else (False, res) 
from Tip import Tip 

class Word: 
    # def countChars(self, word) -> Dict: 
    #     res = {} 
    #     for i in word: 
    #         res[i] = res[i] + 1 if i in res else 1 
    #     return res 

    def __init__(self): 
        self.word = ""  
    
    def getWord(self): 
        return self.word 
    
    def setWord(self, word): 
        self.word = word.upper()  
    
    def calcAccuracy(self, guess): 
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
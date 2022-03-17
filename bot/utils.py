import nextcord 
from Tip import Tip 

def generate_blanks(): 
    return "\N{WHITE MEDIUM SQUARE}" * 5 

def generate_board(): 
    embed = nextcord.Embed(title="Discord Worlde") 
    embed.description = "\n".join([generate_blanks()] * 6) 
    embed.set_footer(text="To play, use the command /play!\n") 
    return embed 

def update_embed(embed: nextcord.Embed, guess, results): 
    empty_slot = generate_blanks() 
    res = "" 
    
    # replace the first blank with the colored word 
    for i, j in enumerate(results): 
        print(guess[i])  
        if j == Tip.CORRECT: 
            res += f"**{guess[i]}**" 
        elif j == Tip.PRESENT: 
            res += f"__{guess[i]}__" 
        else: 
            res += guess[i] 
        res += "     " 

    print(res) 
    embed.description = embed.description.replace(empty_slot, res, 1)
    return embed 
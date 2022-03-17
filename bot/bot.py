import os 
from dotenv import load_dotenv 
import nextcord 
from nextcord.ext import commands 

import utils 
from Game import Game 

# Environment setup 
load_dotenv() 
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN") 
bot = commands.Bot(command_prefix=[]) 

GUILD_IDS = (
    [int(guild_id) for guild_id in os.getenv("GUILD_IDS").split(",")] 
    if os.getenv("GUILD_IDS", None) 
    else nextcord.utils.MISSING 
)

@bot.slash_command(description="Start a new game of Wordle!", guild_ids=GUILD_IDS) 
async def play(interaction: nextcord.Interaction): 
    global game 

    embed = utils.generate_board() 
    game = Game("tempID", "tempName") 
    game.startGame(interaction.user.id) 
    await interaction.send(embed=embed) 

# Event listener for a message being sent to the guild 
@bot.event 
async def on_message(message: nextcord.Message): 
    global game 
    sender = message.author.id 
    req = message.content 
    ref = message.reference 

    # if the message is not a reply 
    if not ref or not isinstance(ref.resolved, nextcord.Message): 
        return 
    
    parent = ref.resolved 
    
    # if the parent message is the not the bot's message 
    if parent.author.id != bot.user.id: 
        return 
    
    # if the message has no embeds 
    if not parent.embeds: 
        return 
    
    embed = parent.embeds[0] 


    if req == "end" and game.isActive(): 
        await message.channel.send(game.endGame(sender)) 
    elif len(req) == 5 and game.isActive(): 
        success, results = game.guess(req, sender) 
        embed = utils.update_embed(embed, req, results)
        await parent.edit(embed=embed) 
        await message.delete() 
    else: 
        await message.reply("Not a valid word!", delete_after=5) 
        await message.delete(delay=5) 

bot.run(DISCORD_TOKEN) 
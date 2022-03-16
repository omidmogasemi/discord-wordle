import os 
import discord 
from dotenv import load_dotenv 
from Game import Game 

# Environment setup 
load_dotenv() 
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN") 
bot = discord.Client() 

# Event listener for the bot's launch 
@bot.event 
async def on_ready(): 
    global game 

    for guild in bot.guilds: 
        print(f"- SERVER ID: {guild.id}, NAME: {guild.name}") 
        game = Game(guild.id, guild.name) 

# Event listener for a message being sent to the guild 
@bot.event 
async def on_message(message): 
    global game 
    sender = message.author.id 
    req = message.content 

    if req == "!start" and not game.isActive(): 
        await message.channel.send(game.startGame(sender)) 
    elif req == "!end" and game.isActive(): 
        await message.channel.send(game.endGame(sender)) 
    elif req[0] == "!" and len(req) == 6 and game.isActive(): 
        await message.channel.send(game.guess(req[1:], sender)) 

bot.run(DISCORD_TOKEN) 
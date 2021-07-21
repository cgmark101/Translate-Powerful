#Import's and libraries
import discord
import os
import random
from discord import message
from discord.ext import commands
from discord.ext.commands.core import check, command
from mtranslate import translate


#Prefix
client = commands.Bot(command_prefix="!", description="Auto-translate Bot")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Test'))
    msg = "Transitor online"
    print(msg)

@client.command()
async def en_es(ctx):
    await ctx.send('Now, Enter the word to translate ')
    
    def check(msg):
        return msg.author == ctx.author and msg.content
    msg = await client.wait_for("message", check=check)
    translate_en_es = translate(msg.content, 'es', 'auto')
    await ctx.send (translate_en_es)
    
    
@client.command()
async def command(ctx):
    computer = random.randint(1, 10)
    await ctx.send('Guess my number')

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and int(msg.content) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    msg = await client.wait_for("message", check=check)

    if int(msg.content) == computer:
        await ctx.send("Correct")
    else:
        await ctx.send(f"Nope it was {computer}")
    

    
    
 #Token
token = os.getenv("DISCORD_TOKEN") 
client.run(token)

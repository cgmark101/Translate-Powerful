#Import's and libraries
import discord
import os
import random
from discord import message
from discord.ext import commands
from discord.ext.commands.core import command
from mtranslate import translate



#Prefix
client = commands.Bot(command_prefix="!", description="Auto-translate Bot")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Test'))
    msg = "Transitor online"
    print(msg)
    
@client.command(name='en_es', help='Translate en-es')
async def en_es(ctx, *, message=''):
    text = ctx.message 
    translate_en_es = translate(text, 'es', 'auto')
    await ctx.send(translate_en_es)
    
    

    
 #Token
token = os.getenv("DISCORD_TOKEN") 
client.run(token)

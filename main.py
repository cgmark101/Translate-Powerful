#Import's and libraries
import discord
import os
import json
from discord import message
from discord.ext import commands
from discord.ext.commands.core import check, command
from mtranslate import translate
from typing import Optional

#Json-Configs
with open ("./config.json") as configjsonFile:
    configData = json.load(configjsonFile)
    LANGUAGE = configData["LANGUAGES"]
    PREFIX = configData["PREFIX_DEFAULT"]
    PRASE = configData["LANGUAGES_PHRASE"]
    

print(LANGUAGE)

#Prefix
client = commands.Bot(command_prefix=PREFIX, description="Auto-translate Bot")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Test'))
    msg = "Transitor online"
    print(msg)
    print(LANGUAGE)
      

@client.command()
async def lang(ctx):
    await ctx.send('Enter the new language, language endings can be found in the help command')
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
    
    msg = await client.wait_for("message", check=check)
    if msg.content == 'es':
        LANGUAGE = "es"
        await ctx.send ('El idioma se ha configurado en español exitosamente')
        print('El lenguaje se ha cambiado a español exitosamente')
    
    if msg.content == 'en':
        LANGUAGE = "en"
        await ctx.send('The language has been set in english successfully')
        print('The language has been set in english successfully')
        





# Universal Translator
@client.command()
async def ts(ctx):
    await ctx.send('frase')
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await client.wait_for("message", check=check)
    translator = translate(msg.content, LANGUAGE, 'auto')
    print(translator)
    await ctx.send (translator)

    
 #Token
token = os.getenv("DISCORD_TOKEN") 
client.run(token)

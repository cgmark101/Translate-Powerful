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


#Prefix
client = commands.Bot(command_prefix=PREFIX, description="Auto-translate Bot")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Test'))
    msg = "Transitor online"
    print(msg)
      

@client.command()
async def lang(ctx):
    await ctx.send('Enter the new language, language endings can be found in the help command')
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
    
    msg = await client.wait_for("message", check=check)

    if msg.content in configData["LANGUAGES"]:
        LANGUAGE = configData["LANGUAGES"][msg.content]
        await ctx.send (LANGUAGE)
        print(LANGUAGE)
    else:
        await ctx.send('The selected language does not exist, enter again, you can check in the help command to know the available languages')
        





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

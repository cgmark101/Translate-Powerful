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
    LANGUAGE = configData["LANGUAGE_DEFAULT"]
    
with open ("./config.json") as f:
    prefixes = json.load(f)
    PREFIX = prefixes["PREFIX_DEFAULT"]

#Prefix
client = commands.Bot(command_prefix=prefixes["PREFIX_DEFAULT"], description="Auto-translate Bot")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Test'))
    msg = "Transitor online"
    print(msg)

# Universal Translator
@client.command()
async def trans(ctx, lang:Optional[str]='es'):
    await ctx.send('Now, Enter a phrase to translate')
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await client.wait_for("message", check=check)
    translate_en_es = translate(msg.content, lang, 'auto')
    await ctx.send (translate_en_es)

    
 #Token
token = os.getenv("DISCORD_TOKEN") 
client.run(token)

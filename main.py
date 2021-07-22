#Import's and libraries
import discord
import os
import json
from discord import message
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.core import check, command
from mtranslate import translate
from typing import Optional

#Json-Configs
with open ("./config.json") as configjsonFile:
    configData = json.load(configjsonFile)


#Prefix
client = commands.Bot(command_prefix=configData["PREFIX_DEFAULT"], description="Auto-translate Bot")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Google-Translate'))
    msg = "Transitor online"
    print(msg)
    print(os.getenv("LANG"))
      

@client.command()
async def lang(ctx):
    await ctx.send('Enter the new language, language endings can be found in the help command')
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
    
    msg = await client.wait_for("message", check=check, timeout=30)

    if msg.content.lower() in configData["LANGUAGES"]:
        os.environ["LANG"] = msg.content
        LANG = configData["LANGUAGES"][msg.content]
        await ctx.send (LANG)
        print(LANG)
    
    elif msg.content.lower() == "cn":
        LANG = "zh-CN"
        if LANG in configData["LANGUAGES"]:
            os.environ["LANG"] = LANG
            LANG = configData["LANGUAGES"][LANG]
            await ctx.send (LANG)
            print(LANG)
        
    else:
        await ctx.send('The selected language does not exist, enter again, you can check in the help command to know the available languages')
        
#help command
@client.command()
async def embed(ctx):
    embed=discord.Embed(title="Help menu", url="https://realdrewdata.medium.com/", description="English - en", color=discord.Color.red())
    await ctx.send(embed=embed)


# Universal Translator
@client.command()
async def ts(ctx, aliases=['tss', 'traslate']):
    LANG = os.getenv("LANG")
    await ctx.send(configData["LANGUAGES_PHRASE"][LANG])
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await client.wait_for("message", check=check)
    translator = translate(msg.content, LANG, 'auto')
    print(translator)
    await ctx.send (translator)

 #Token
token = os.getenv("DISCORD_TOKEN") 
client.run(token)

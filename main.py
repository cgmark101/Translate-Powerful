#Import's and libraries
import discord
import os
import json
from discord import message
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.core import check, command
from trans.mark1 import translate

#Json-Configs
with open ("./config.json") as configjsonFile:
    configData = json.load(configjsonFile)


#Prefix
client = commands.Bot(command_prefix=configData["PREFIX_DEFAULT"], description="Auto-translate Bot")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Google-Translate'))
    msg = "Translate online"
    print(msg)

    
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
async def helper(ctx):
    helper=discord.Embed(title="Help Menu", url="https://www.google.com", description="Translate Help Menu - Commands and example of use", color=0x006eff)
    helper.set_author(name="Translate  Auto-Translate Bot", url="https://translate.google.com/", icon_url="https://i.ibb.co/YZxpyz2/google-translate-icon-by-spideyforever2005-dc0xsrb.png")
    helper.set_thumbnail(url="https://i.ibb.co/YZxpyz2/google-translate-icon-by-spideyforever2005-dc0xsrb.png")
    helper.add_field(name="URL-WEB XD", value="In this web explain how to use commands and configuration")
    await ctx.send(embed=helper)




#Information Command
@client.command()
async def info(ctx):
    
    info=discord.Embed(title="Information Bot", url="https://translate.google.com/", description="Information about translate bot, version and authors", color=0x006eff)
    info.set_author(name="Auto-Translate bot", url="https://i.ibb.co/YZxpyz2/google-translate-icon-by-spideyforever2005-dc0xsrb.png", icon_url="https://i.ibb.co/YZxpyz2/google-translate-icon-by-spideyforever2005-dc0xsrb.png")
    info.set_thumbnail(url="https://i.ibb.co/YZxpyz2/google-translate-icon-by-spideyforever2005-dc0xsrb.png")
    info.add_field(name="Description", value=configData["Info"]["Description"], inline=False)
    info.add_field(name="Version", value=configData["Info"]["Version"], inline=False)
    info.add_field(name="Authors", value=configData["Info"]["Authors"], inline=False)
    await ctx.send(embed=info)


# Universal Translator
@client.command()
async def ts(ctx):
    LANG = os.getenv("LANG")
    await ctx.send(configData["LANGUAGES_PHRASE"][LANG])
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await client.wait_for("message", check=check, timeout=30)
    translator = translate(msg.content, LANG, 'auto')
    print(translator)
    await ctx.send (translator)

 #Token
token = os.getenv("DISCORD_TOKEN") 
client.run(token)

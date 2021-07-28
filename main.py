#Import's and libraries
import discord
import os
import json
from discord import message
from discord import activity
from discord import guild
from discord import embeds
from discord.activity import Activity, create_activity
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.converter import _get_from_guilds
from discord.ext.commands.core import check, command
from discord.ext.commands.errors import GuildNotFound
from trans.mark1 import translate
from tinydb import TinyDB, Query
from tinydb.operations import delete

#Database
db = TinyDB('db.json')



#Json-Configs
with open ("./config.json") as configjsonFile:
    configData = json.load(configjsonFile)


#Prefix

client = commands.Bot(command_prefix=os.getenv("PREFIX_DEFAULT"), description="Auto-translate Bot")

@client.event
async def on_guild_join(Guild):
    print(f'I have joined a {str(Guild.name)}')
    db.insert({
        'name_server':Guild.name,
        'id_server':Guild.id
    })
    insert = db.insert
    print(insert)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"on {str(len(client.guilds))} servers"))
    msg = "Translate Powerful online"
    print(msg)

# Delete existing help command for create new help command with embed
client.remove_command("help")

@client.command()
@commands.has_permissions(administrator=True)
async def lang(ctx):
    trans=discord.Embed(title="Language set", url="https://translate.google.com/", description=f'{ctx.author.mention}: Enter the new language, language endings can be found in the help command', color=0x006eff)

    await ctx.send(embed=trans)
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
    
    msg = await client.wait_for("message", check=check, timeout=30)

    if msg.content.lower() in configData["LANGUAGES"]:
        os.environ["LANG"] = msg.content
        LANG = configData["LANGUAGES"][msg.content]
        trans=discord.Embed(title="Language set", description=LANG, color=0x006eff)
        await ctx.send (embed=trans)
        print(LANG)
    
    elif msg.content.lower() == "cn":
        LANG = "zh-CN"
        if LANG in configData["LANGUAGES"]:
            os.environ["LANG"] = LANG
            LANG = configData["LANGUAGES"][LANG]
            await ctx.send (LANG)
            print(LANG)
        
    else:
        trans=discord.Embed(title="Translate Error", description=f'{ctx.author.mention}: The selected language does not exist, enter again, you can check in the help command to know the available languages', color=0x006eff)
        await ctx.send(embed=trans)
        
        
#help command
@client.command()
async def help(ctx):
    help=discord.Embed(title="Help Menu", url="https://translate.google.com/", description="Translate Help Menu - Commands and example of use", color=0x006eff)
    help.set_author(name="Translate", url="https://i.ibb.co/YZxpyz2/google-translate-icon-by-spideyforever2005-dc0xsrb.png", icon_url="https://i.ibb.co/YZxpyz2/google-translate-icon-by-spideyforever2005-dc0xsrb.png")
    help.set_thumbnail(url="https://i.ibb.co/YZxpyz2/google-translate-icon-by-spideyforever2005-dc0xsrb.png")
    help.add_field(name="Commands", value="LINK", inline=True)
    help.add_field(name="Languages Supported", value="LINK", inline=False)
    await ctx.send(embed=help)




#Information Command
@client.command()
async def info(ctx):
    
    info=discord.Embed(title="Information Bot", url="https://translate.google.com/", description="Information about translate bot, version and authors", color=0x006eff)
    info.set_author(name="Translate Powerful", url="https://i.ibb.co/YZxpyz2/google-translate-icon-by-spideyforever2005-dc0xsrb.png", icon_url="https://i.ibb.co/YZxpyz2/google-translate-icon-by-spideyforever2005-dc0xsrb.png")
    info.set_thumbnail(url="https://i.ibb.co/YZxpyz2/google-translate-icon-by-spideyforever2005-dc0xsrb.png")
    info.add_field(name="Description", value=configData["Info"]["Description"], inline=False)
    info.add_field(name="Version", value=configData["Info"]["Version"], inline=False)
    info.add_field(name="Authors", value=configData["Info"]["Authors"], inline=False)
    await ctx.send(embed=info)


# Universal Translator
@client.command()
async def ts(ctx):
    LANG = os.getenv("LANG")
    phrase_language = configData["LANGUAGES_PHRASE"][LANG]
    phrase_embed =discord.Embed(title='Translate', description=f'{phrase_language}', color=0x006eff)
    await ctx.send(embed=phrase_embed)
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await client.wait_for("message", check=check, timeout=30)
    translator = translate(msg.content, LANG, 'auto')
    translator_embed=discord.Embed(title="Translate", description=f'{ctx.author}: {translator}', color=0x006eff)
    await ctx.send (embed=translator_embed)

 #Token
token = os.getenv("DISCORD_TOKEN") 
client.run(token)

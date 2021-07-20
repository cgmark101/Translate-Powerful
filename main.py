# Import's and libraries
import os
import random
from dotenv import load_dotenv
from discord.ext import commands
from mtranslate import translate

#Save token in secret file :)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Prefix bot
bot = commands.Bot(command_prefix='t!')

#Print log after bot run
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

bot.run(TOKEN)

import disnake
from disnake.ext import commands
import os
from flask import Flask 
from threading import Thread

bot = commands.Bot(
	command_prefix="sb ",
	activity=disnake.Game(name=f"disnake {disnake.__version__}"),
	help_command=None,
	case_insensitive=True,
	test_guilds=[866991015584071691, 808030843078836254]
)

# Extensions
bot.load_extension("cogs.faq")

@bot.event
async def on_ready():
    print(disnake.__version__)
    print('Logged in as {0.user}'.format(bot))

bot.run(os.getenv('TOKEN'))

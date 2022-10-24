import discord
from dotenv import load_dotenv
from get_data import set_var_dotenv

#========================== INITIALIZE VARIABLE ==========================#
bot = discord.Client()
#========================== MAIN ==========================#

load_dotenv(override = True)
TOKEN = set_var_dotenv("DISCORD_TOKEN")
@bot.event
async def on_ready():
    print("Bot online")
bot.run(TOKEN)

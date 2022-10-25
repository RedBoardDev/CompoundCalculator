import discord
from discord.ext import commands
from dotenv import load_dotenv
from get_data import set_var_dotenv

#========================== INITIALIZE VARIABLE ==========================#
intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix="$")
#========================== MAIN ==========================#

# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.CommandNotFound):
#         await ctx.send("Unknown command, please refer to $help")

# @bot.command(name="dcompound")
# async def received_message_cmd(ctx, test: int):
#     await ctx.message.delete()
#     await ctx.author.send(test)

load_dotenv(override = True)
TOKEN = set_var_dotenv("DISCORD_TOKEN")
@bot.event
async def on_ready():
    print("Bot online")
    await bot.load_extension("commands")
bot.run(TOKEN)

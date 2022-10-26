from python_algo import calculate_optimum_compound_days, calculate_gross_rewards, calculate_nbrs_of_periods
from discord.ext import commands

class Commands_all(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="dcompound")
    async def received_message_cmd(self, ctx, initialInvestment:float, APR:int, frequency:str):
        await ctx.message.delete()
        frequency_list = ['monthly', 'daily', 'hourly', 'minute']
        # if (frequency in frequency_list):
        if (initialInvestment > 0 and APR > 0):
            # gasCost:float = get_actual_gasCost()
            gasCost:float = 0.1
            optimumCompoundDays:float = calculate_optimum_compound_days(frequency, gasCost, APR, initialInvestment)
            message:str = "The best option is compound every " + (str)(round(optimumCompoundDays, 2)) + " " + frequency
            optimum_nbrs_of_periods:float = calculate_nbrs_of_periods(frequency, optimumCompoundDays)
            optimum_grossRewards:float = calculate_gross_rewards(optimum_nbrs_of_periods, gasCost, APR, initialInvestment)
            message += "\nYou can earn " + (str)(round(optimum_grossRewards, 2)) + "$ in 1 year with this APR"
            await ctx.author.send(message)
        else:
            await ctx.send("Error: please, dont put an equal at 0 or negatif initialInvestment / APR")
        # else:
        #     await ctx.send("Error: wrong frequency.\nPlease use one on this list: monthly, daily, hourly, minute")

    @received_message_cmd.error
    async def received_message_error(self, ctx, error: commands.CommandError):
        if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send('Error: $dcompound initialInvestment APR frequency')
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found...')
        elif isinstance(error, commands.BadArgument):
            error_message = "Error: $dcompound initialInvestment APR frequency"
            error_message += "\ninitialInvestment - your investment in $"
            error_message += "\nAPR - actual APR in %"
            error_message += "\nfrequency - plage of frequency of compound (monthly, daily, hourly, minute)"
            error_message += "\nExample: *$dcompound 100 742 daily*"
            await ctx.send(error_message)

async def setup(bot):
    await bot.add_cog(Commands_all(bot))

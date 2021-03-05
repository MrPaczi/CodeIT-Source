import discord
from discord.ext import commands
from datetime import datetime
import asyncio
import random
import os

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Giveaway ready!!")

@client.command()
@commands.has_permissions(administrator = True)
async def gstart(ctx, mins : int, * , prize: str):

    user = ctx.author

    end = datetime.now().strftime('%H:%M')

    embed = discord.Embed(title = f"{prize}", description = f"Ends at: {end}\nHosted by: {user.mention}", color = discord.Color.dark_blue())
    embed.set_footer(text = f"Ends {mins} minutes from now!")

    my_msg = await ctx.send("**🎉GIVEAWAY!🎉**", embed = embed)

    await my_msg.add_reaction("🎉")


    new_msg = await ctx.channel.fetch_message(my_msg.id)

    users = new_msg.reactions[0].users().flatten()
    users.pop(user.index(client.user))

    winner = random.choice(users)

    await asyncio.sleep(mins*60)

    await ctx.send(f"Congratulations! {winner.mention} won {prize}!")

client.run("ODE0NTY4MDYyNjA2NzcwMjM2.YDfvoA.OmfBHbMXHOvwPWWsB87RDv2ZswI")
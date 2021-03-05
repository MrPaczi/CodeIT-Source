import discord
from discord.ext import commands
import os
from datetime import datetime

client = commands.Bot(command_prefix="!")
time = datetime.now().strftime('%H:%M')

@client.event
async def on_ready():
  print('Report ready!!')

@client.command()
async def report(ctx, member: discord.Member, reason = None):

  user = ctx.author

  if (reason == None):
    no_ = discord.Embed(description="Podaj powód dlaczego zgłaszasz użytkownika!", color = discord.Color.dark_blue())
    no_.set_footer(text=f"Dziś {time}! By CodeIT Discord Bot!")
    await ctx.send(embed=no_)
  else:
    eport = discord.Embed(title=f"Zgłoszono {member.name}#{member.discriminator}", description = f"Zgłoszono  {member.mention} przez {user.mention}!", color = discord.Color.dark_blue())
    eport.set_footer(text=f"Dziś {time}! By CodeIT Discord Bot!")
    await ctx.send(embed=eport)

    report = discord.Embed(title=f"Zostałeś zgłoszony przez {user.name}#{user.discriminator}!", description=f"Zostałeś zgłoszony przez użytkownika {user.name}#{user.discriminator}! Jesteś teraz pod czujnym okiem administracji! Lepiej uważaj!", color = discord.Color.dark_blue())
    report.add_field(name="Reported by:", value=f"{user.name}#{user.discriminator}", inline=False)
    report.add_field(name="Reported user:", value=f"{member.name}#{member.discriminator}", inline=False)
    report.add_field(name="Reason:", value=f"{reason}", inline=False)
    report.set_footer(text=f"Dziś {time}! By CodeIT Discord Bot!")
    await member.send(embed=report)

client.run("ODE0NTY4MDYyNjA2NzcwMjM2.YDfvoA.OmfBHbMXHOvwPWWsB87RDv2ZswI")
import discord
from discord.ext import commands
from datetime import datetime

client = commands.Bot(command_prefix="!")
time = datetime.now().strftime('%H%M')

@client.event
async def on_ready():
    print("Admin Commands ready!!")

@client.command()
@commands.has_permissions(administrator = True)
async def ban(ctx, member : discord.Member, *, reason=None):

    user = ctx.author

    if (reason == None):
        nope = discord.Embed(description="Podaj powód bana użytkownika!", color = discord.Color.dark_blue())
        nope.set_footer(text=f"Dziś {time}! By CodeIT Discord Bot!")
        await ctx.send(embed=nope)
    else:
        nope = discord.Embed(title=f"Zostałeś zbanowany przez {user.name}#{user.discriminator}!", color = discord.Color.dark_blue())
        nope.add_field(name="Banned by:", value = f"{user.name}{user.discriminator}", inline=False)
        nope.add_field(name="Banned user:", value = f"{member.name}#{member.discriminator}", inline=False)
        nope.add_field(name="Reason:", value=f"{reason}", inline=False)
        nope.add_field(name="Odwołanie:", value="Odwołanie możesz złożyć u administracji!", inline=False)
        nope.set_footer(text=f"Dziś {time}! By CodeIT Discord Bot!")
        await member.send(embed=nope)

        ad_ = discord.Embed(title=f"Zbanowa {member.name}#{member.discriminator}!", description=f"Zbanowano użytkownika {member.name}#{member.discriminator}! Powód: {reason}!", color = discord.Color.dark_blue())
        await ctx.send(embed=ad_)

        await member.ban(reason=reason)

@client.command()
@commands.has_permissions(administrator = True)
async def kick(ctx, member : discord.Member, *, reason=None):

    user = ctx.author

    if (reason == None):
        nope = discord.Embed(description="Podaj powód wyrzucenia użytkownika!", color = discord.Color.dark_blue())
        nope.set_footer(text=f"Dziś {time}! By CodeIT Discord Bot!")
        await ctx.send(embed=nope)
    else:
        nope = discord.Embed(title=f"Zostałeś wyrzucony przez {user.name}#{user.discriminator}!", color = discord.Color.dark_blue())
        nope.add_field(name="Kicked by:", value = f"{user.name}{user.discriminator}", inline=False)
        nope.add_field(name="Kicked user:", value = f"{member.name}#{member.discriminator}", inline=False)
        nope.add_field(name="Reason:", value=f"{reason}", inline=False)
        nope.add_field(name="Odwołanie:", value="Odwołanie możesz złożyć u administracji!", inline=False)
        nope.set_footer(text=f"Dziś {time}! By CodeIT Discord Bot!")
        await member.send(embed=nope)

        ad_ = discord.Embed(title=f"Wyrzucono {member.name}#{member.discriminator}!", description=f"Wyrzucono użytkownika {member.name}#{member.discriminator}! Powód: {reason}!", color = discord.Color.dark_blue())
        await ctx.send(embed=ad_)

        await member.kick(reason=reason)

@client.command()
@commands.has_permissions(administrator = True)
async def mute(ctx, member : discord.Member, reason=None):

    user = ctx.author

    if (reason == None):
        nope = discord.Embed(description="Podaj powód zmutowania użytkownika!", color = discord.Color.dark_blue())
        nope.set_footer(text=f"Dziś {time}! By CodeIT Discord Bot!")
        await ctx.send(embed=nope)
    else:
        # pobieramy ID roli Muted która jest na serverze czyli Guild
        role = discord.utils.get(member.guild.roles, name='Muted')
        print(role)

        if (role is not None):
            # ustawia memberowi rolę Muted
            await member.add_roles(role)

            nope = discord.Embed(title=f"Zostałeś zmutowany przez {user.name}#{user.discriminator}!", color = discord.Color.dark_blue())
            nope.add_field(name="Muted by:", value = f"{user.name}{user.discriminator}", inline=False)
            nope.add_field(name="Muted user:", value = f"{member.name}#{member.discriminator}", inline=False)
            nope.add_field(name="Reason:", value=f"{reason}", inline=False)
            nope.add_field(name="Odwołanie:", value="Odwołanie możesz złożyć u administracji!", inline=False)
            nope.set_footer(text=f"Dziś {time}! By CodeIT Discord Bot!")
            await member.send(embed=nope)

            ad_ = discord.Embed(title=f"Zmutowano {member.name}#{member.discriminator}!", description=f"Zmutowano użytkownika {member.name}#{member.discriminator}! Powód: {reason}!", color = discord.Color.dark_blue())
            await ctx.send(embed=ad_)


@client.command()
@commands.has_permissions(administrator = True)
async def unmute(ctx, member : discord.Member = None):

    user = ctx.author

    if (member == None):
        nope = discord.Embed(description="Podaj użytkownika, którego chcesz odciszyć!", color = discord.Color.dark_blue())
        nope.set_footer(text=f"Dziś {time}! By CodeIT Discord Bot!")
        await ctx.send(embed=nope)
    else:

        role = discord.utils.get(member.guild.roles, name='Muted')
        print(role)

        if (role is not None):
            # ustawia memberowi rolę Muted
            await member.remove_roles(role)

            nope = discord.Embed(title=f"Zostałeś odmutowany przez {user.name}#{user.discriminator}!", color = discord.Color.dark_blue())
            nope.add_field(name="Unmuted by:", value = f"{user.name}{user.discriminator}", inline=False)
            nope.add_field(name="Unmuted user:", value = f"{member.name}#{member.discriminator}", inline=False)
            nope.set_footer(text=f"Dziś {time}! By CodeIT Discord Bot!")
            await member.send(embed=nope)

            ad_ = discord.Embed(title=f"Odmutowano {member.name}#{member.discriminator}!", description=f"Odmutowano użytkownika {member.name}#{member.discriminator}!", color = discord.Color.dark_blue())
            await ctx.send(embed=ad_)

@client.command()
@commands.has_permissions(administrator = True)
async def warn(ctx, member: discord.Member, reason=None):

    user = ctx.author

    if (reason == None):
        nope = discord.Embed(description="Podaj powód warna dla użytkownika!", color = discord.Color.dark_blue())
        nope.set_footer(text=f"Dziś {time}! By CodeIT Discord Bot!")
        await ctx.send(embed=nope)
    else:
        nope = discord.Embed(title=f"Zostałeś ostrzeżony przez {user.name}#{user.discriminator}!", color = discord.Color.dark_blue())
        nope.add_field(name="Warned by:", value = f"{user.name}{user.discriminator}", inline=False)
        nope.add_field(name="Warned user:", value = f"{member.name}#{member.discriminator}", inline=False)
        nope.add_field(name="Reason:", value=f"{reason}", inline=False)
        nope.add_field(name="Odwołanie:", value="Odwołanie możesz złożyć u administracji!", inline=False)
        nope.set_footer(text=f"Dziś {time}! By CodeIT Discord Bot!")
        await member.send(embed=nope)

        ad_ = discord.Embed(title=f"Ostrzeżono {member.name}#{member.discriminator}!", description=f"Ostrzeżono użytkownika {member.name}#{member.discriminator}! Powód: {reason}!", color = discord.Color.dark_blue())
        await ctx.send(embed=ad_)

client.run("ODE0NTY4MDYyNjA2NzcwMjM2.YDfvoA.OmfBHbMXHOvwPWWsB87RDv2ZswI")
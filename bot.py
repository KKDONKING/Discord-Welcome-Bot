import discord
import datetime
from coin_flip import coin_flip
from discord.ext import commands

intents = discord.Intents.all()
discord.member = True

role_channel = 1132860437923381298 # role channel id goes here
bot = commands.Bot(command_prefix="$", intents = discord.Intents.all())

@bot.event
async def on_ready():  
    print("Bot is online") 

@bot.event
async def on_message(message):
    if message.content == "I'm alive":
        embed = discord.Embed(
            description=f"You should go and KYS Now!"
        )
        embed.set_image(url="https://media.tenor.com/67LIumILNRsAAAAd/ltg-low-tier-god.gif")
        await message.reply(embed=embed)

    
@bot.event 
async def on_member_join(member):
    print(f"{member} joined")
    channel = member.guild.system_channel
    embed = discord.Embed(
        description=f'Welcome **{member.mention}** to the server',
        colour=discord.Colour.random(),
        timestamp=datetime.datetime.now(),
       
    )
    embed.add_field(name=f"You can get your role in <#{role_channel}>", value="")
    embed.set_thumbnail(url=f"{member.display_avatar}")
    await channel.send(embed=embed)

@bot.event 
async def on_member_remove(member):
    print(f"{member} left")
    channel = member.guild.system_channel
    embed = discord.Embed(
        description=f'Rip **{member.mention}** Bozo',
        colour=discord.Colour.random(),
        timestamp=datetime.datetime.now(),   
    )
    embed.add_field(name=f"You won't be missed", value="")
    embed.set_thumbnail(url=f"{member.display_avatar}")
    embed.set_image(url="https://media.tenor.com/OYp_uK4WcwkAAAAd/packwatch-ripbozo.gif")
    await channel.send(embed=embed)
#stupid essh bot

@bot.event
async def on_message(message):
    print("essh command received")
    if message.content == "I'm alive".lower():
        embed = discord.Embed()
        embed.set_image(url="https://media.tenor.com/67LIumILNRsAAAAd/ltg-low-tier-god.gif")
        await message.reply(embed=embed)
    else:
        return
@bot.command()
async def coin_toss(ctx, member: discord.Member = None):
    print("coin_toss command invoked")
    if member is None:
        member = ctx.author
    coin_flipped, coin_sides = coin_flip()
    coin_toss = discord.Embed(
        title=f"{member.name} flipped a coin",
        description=f'It\'s a **{coin_flipped}**',
        colour=discord.Colour.random(),
    )
    coin_toss.set_thumbnail(url=f"{coin_sides}")
    await ctx.send(embed=coin_toss)
bot.run("NzQxMzYzOTk2NzI4MzYwOTcw.GLI0B6.FrpSP8P3DNcTdI9bu8io5sH9KV9y6lLq4N7VBA") #add the bot token inside the double quotes

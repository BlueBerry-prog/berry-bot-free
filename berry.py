import discord
import asyncio
from discord.ext import commands
from discord import utils
from discord.ext.commands import Bot
from discord.utils import get

bot = commands.Bot(command_prefix = '$')
bot.remove_command('help')


bad_words=['pl','com','.gg','net','io',]



@bot.event
async def on_ready():
    print ("----------------")
    print('|  Berry-BOT |ON|')
    print ('----------------')
    print('\/_\/_\/_\/_\/_\/')
    print('---------------------')
    print('| Autor :Blueberry  |')
    print("---------------------")
    await bot.change_presence(status = discord.Status.idle, activity = discord.Game('$help | Chesz bota na swojego discord? psiz do 🍇BlueBerry🍇#1337'))
    global my_channel
    my_channel = bot.get_channel(819635116925517904)
    await my_channel.send(content='Bot starting...')
    await my_channel.send(content='Loading...[][][][][][][][][][] 0%')
    await asyncio.sleep(2)
    await my_channel.send(content="Loading... █[][][][][][][][][] 10%")
    await asyncio.sleep(1)
    await my_channel.send(content="Loading... ██[][][][][][][][] 20%")
    await asyncio.sleep(4)
    await my_channel.send(content="Loading... ███[][][][][][][] 30%")
    await asyncio.sleep(1)
    await my_channel.send(content="Loading... ████[][][][][][] 40%")
    await asyncio.sleep(1)
    await my_channel.send(content="Loading... █████[][][][][] 50%")
    await asyncio.sleep(2)
    await my_channel.send(content="Loading... ███████[][][][] 60%")
    await asyncio.sleep(3)
    await my_channel.send(content="Loading... ████████[][][] 70%")
    await asyncio.sleep(4)
    await my_channel.send(content="Loading... █████████[][] 80%")
    await asyncio.sleep(1)
    await my_channel.send(content="Loading... ██████████[] 90%")
    await asyncio.sleep(2)
    await my_channel.send(content="Loading... ███████████100%")
    await my_channel.send(content="I'am Ready")


#bad
@bot.event
async def on_message(message):
    for a in bad_words:
        if a in message.content:
            await message.delete()
            await message.channel.send('``Nie reklamuj sie``')
    await bot.process_commands(message)


#clear
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit=amount+1)




#help
@bot.command(pass_context = True)
async def help(ctx,*args, amount = 1):
    helped = ("""```Fix\n-|-Komendy Dla graczy-|-\n$autor\n-|-Komendy Administracji-|-\n$clear liczba\n$ban @czlowek\n$kick @czlowek\n$mute @czlowek+time\n$addrole @czlowek @rola +time\n```""")
    embed = discord.Embed(title="Help-pl",colour=discord.Colour.blue())
    embed.add_field(name="commands",value=helped)
    await ctx.channel.purge( limit = amount )
    await ctx.send(embed=embed)

#mute
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member, time:int,  reason="none", amount = 1):
    muterole = discord.utils.get(ctx.message.guild.roles,name='⛔️ | zmutowany')
    comrole = discord.utils.get(ctx.message.guild.roles,name='🌍 | Comiunity')
    embed=discord.Embed(title="Was muted",colour=member.colour,timestamp=ctx.message.created_at)
    embed.add_field(name='Admin:',value=ctx.message.author.mention)
    embed.add_field(name='Szkodnik:',value=member.mention)
    embed.add_field(name='Czas:',value=time)
    embed.add_field(name='Reason:',value=reason)
    await member.add_roles(muterole)
    await member.remove_roles(comrole)
    await ctx.channel.purge( limit = amount )
    await ctx.send(embed = embed)
    await asyncio.sleep(time * 60)
    await member.remove_roles(muterole)
    await member.add_roles(comrole)





#give role
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def addrole(ctx, member: discord.Member, role: discord.Role,time:int):
    embed=discord.Embed(title="Rangi-Log")
    embed.add_field(name='Admin:',value=ctx.message.author.mention,inline=False)
    embed.add_field(name='User:',value=member.mention,inline=False)
    embed.add_field(name='Rola:',value=role.mention,inline=False)
    embed.add_field(name=f'Czas: {time} m', value="؜؜",inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(role)
    await asyncio.sleep(time * 60)
    await member.remove_roles(role)


#Ban
@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason="po prostu", amount = 1):
        await member.ban(reason=reason)
        ban = discord.Embed(title=f":boom: Was banned {member.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=ban)
        await ctx.channel.purge( limit = amount )
        await ctx.send(embed=ban)


#kick
@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason="poprostu", amount = 1):
        await member.kick(reason=reason)
        kick = discord.Embed(title=f":boom: Was kicked{member.name}!", description=f"Reason: {reason}")
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await ctx.channel.purge( limit = amount )
        await ctx.send(embed=kick)


#Autor
@bot.command(pass_context = True)
async def autor(ctx,*args, amount = 1):
    helped = ("""```Fix\n-|-Autor:BlueBerry-|-\n```""")
    embed = discord.Embed(title="Autor:BerryBot-Free",colour=discord.Colour.blue())
    embed.add_field(name="-------------",value=helped)
    await ctx.channel.purge( limit = amount )
    await ctx.send(embed=embed)


bot.run('ODA5ODQxOTEwNzUxMTY2NDg0.YCa-DQ.ZhEkKz6iniU_tIDl0jy0_W3taAA')

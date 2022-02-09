import asyncio
import os
from asyncio import sleep

import discord
import sys
import random
from discord.ext import commands
import tiktok_db as tiktok
import sqlite3 as sl

token = ''

bot = commands.Bot(command_prefix='+')


consumer_key = ''
consumer_secret = ''
access_token_key = ''
access_token_secret = ''

requests = []


# @bot.event
# async def on_message(message):
#     if message.author.id == 359223912585756672:
#         channel = message.channel
#         await channel.send('<@!359223912585756672> double neg btw')
#
#         #def check(m):
#         #    return m.content == 'hello' and m.channel == channel
#
#         # msg = await bot.wait_for('message', check=check)
#         # await channel.send('Hello {.author}!'.format(msg))



@bot.command(name='addfmbl')
async def add_fmbl(ctx, *, reason=""):
    if reason != "":
        tiktok.update_fumble(ctx.author, reason)
    fumbles = tiktok.add_fmbl()
    for x in fumbles:
        how_many = str(x[0])
        await ctx.send(how_many + " fumbles")


@bot.command(name='subfmbl')
async def sub_fmbl(ctx):
    fmbles = tiktok.sub_fmbl()
    for x in fmbles:
        fumbles = str(x[0])
        print(x[0])
        await ctx.send(fumbles + " fumbles")


@bot.command(name='viewfumbles')
async def view_fumbles(ctx):
    fumbles = tiktok.get_reasons()
    embed = discord.Embed(title='List of Fumbles', description="Wall of Shame", color=0x00ff00)
    for reason in fumbles:
        if reason[1] != "":
            embed.add_field(name=reason[0], value=f'> Reason: {reason[1]}\n> UniqueID: {reason[2]}', inline=False)
    await ctx.send(embed=embed)


@bot.command(name='accountability')
async def view_fumbles(ctx):
    await ctx.send("Where's the consistency bitch")


@bot.command(name='doubleneg')
async def neg(ctx):
    await ctx.send(ctx.author.display_name + " went double negative in league play")


@bot.command(name='removefumble')
async def delete_fumbles(ctx, id):
    p = tiktok.remove_fumble(ctx.author, id)
    await ctx.send(p)


@bot.command(name="monitor", help='Blank')
async def reddit(ctx):
    pass

@bot.command(name='bussit', help='tiktok!')
async def buss_it(ctx):
    selectedTikTok = tiktok.pick_random_link()
    await ctx.send("Fumbles")
    for x in selectedTikTok:
        username = x[0]
        link = x[1]
        desc = "Their username is " + username
        embed = discord.Embed(title='Yuhh buss it', description=link, color=0x00ff00)
        embed.add_field(name="username", value=desc, inline=False)
        await ctx.send(embed=embed)
        break


@bot.command(name='clownbozo', help="dun dun duna duna dunaaa")
async def clown(ctx):
    source = discord.PCMVolumeTransformer(
        discord.FFmpegPCMAudio(executable='C:\\Users\\juanl\\Desktop\\ffmpeg\\bin\\ffmpeg.exe',
                               source='clown.mp3'))
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = await voice_channel.connect()
        vc.play(source)
        while vc.is_playing():  # Checks if voice is playing
            await asyncio.sleep(1)  # While it's playing it sleeps for 1 second
        else:
            await asyncio.sleep(5)  # If it's not playing it waits 15 seconds
            while vc.is_playing():  # and checks once again if the bot is not playing
                break  # if it's playing it breaks
            else:
                await vc.disconnect()  # if not it disconnects


@bot.command(name='astrid', help="a girl named astrid")
async def astrid(ctx):
    source = discord.PCMVolumeTransformer(
        discord.FFmpegPCMAudio(executable='C:\\Users\\juanl\\Desktop\\ffmpeg\\bin\\ffmpeg.exe',
                               source='astrid.mp3'))
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = await voice_channel.connect()
        vc.play(source)
        while vc.is_playing():  # Checks if voice is playing
            await asyncio.sleep(1)  # While it's playing it sleeps for 1 second
        else:
            await asyncio.sleep(5)  # If it's not playing it waits 15 seconds
            while vc.is_playing():  # and checks once again if the bot is not playing
                break  # if it's playing it breaks
            else:
                await vc.disconnect()  # if not it disconnects


@bot.command(name='dog', help="this is me")
async def dog(ctx):
    source = discord.PCMVolumeTransformer(
        discord.FFmpegPCMAudio(executable='C:\\Users\\juanl\\Desktop\\ffmpeg\\bin\\ffmpeg.exe',
                               source='dog.mp3'))
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = await voice_channel.connect()
        vc.play(source)
        while vc.is_playing():  # Checks if voice is playing
            await asyncio.sleep(1)  # While it's playing it sleeps for 1 second
        else:
            await asyncio.sleep(5)  # If it's not playing it waits 15 seconds
            while vc.is_playing():  # and checks once again if the bot is not playing
                break  # if it's playing it breaks
            else:
                await vc.disconnect()  # if not it disconnects


@bot.command(name='chill', help="daddy")
async def chill(ctx):
    source = discord.PCMVolumeTransformer(
        discord.FFmpegPCMAudio(executable='C:\\Users\\juanl\\Desktop\\ffmpeg\\bin\\ffmpeg.exe',
                               source='daddy.mp3'))
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = await voice_channel.connect()
        vc.play(source)
        while vc.is_playing():  # Checks if voice is playing
            await asyncio.sleep(1)  # While it's playing it sleeps for 1 second
        else:
            await asyncio.sleep(5)  # If it's not playing it waits 15 seconds
            while vc.is_playing():  # and checks once again if the bot is not playing
                break  # if it's playing it breaks
            else:
                await vc.disconnect()  # if not it disconnects


@bot.command(name='what', help="WHAT")
async def what(ctx):
    source = discord.PCMVolumeTransformer(
        discord.FFmpegPCMAudio(executable='C:\\Users\\juanl\\Desktop\\ffmpeg\\bin\\ffmpeg.exe',
                               source='what.mp3'))
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = await voice_channel.connect()
        vc.play(source)
        while vc.is_playing():  # Checks if voice is playing
            await asyncio.sleep(1)  # While it's playing it sleeps for 1 second
        else:
            await asyncio.sleep(5)  # If it's not playing it waits 15 seconds
            while vc.is_playing():  # and checks once again if the bot is not playing
                break  # if it's playing it breaks
            else:
                await vc.disconnect()  # if not it disconnects


@bot.command(name='thangin', help="Andres be bhoolin")
async def thangin(ctx):
    source = discord.PCMVolumeTransformer(
        discord.FFmpegPCMAudio(executable='C:\\Users\\juanl\\Desktop\\ffmpeg\\bin\\ffmpeg.exe',
                               source='thangin.mp3'))
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = await voice_channel.connect()
        vc.play(source)
        while vc.is_playing():  # Checks if voice is playing
            await asyncio.sleep(1)  # While it's playing it sleeps for 1 second
        else:
            await asyncio.sleep(5)  # If it's not playing it waits 15 seconds
            while vc.is_playing():  # and checks once again if the bot is not playing
                break  # if it's playing it breaks
            else:
                await vc.disconnect()  # if not it disconnects


@bot.command(name='juan', help="Juan you can't say that")
async def chill(ctx):
    source = discord.PCMVolumeTransformer(
        discord.FFmpegPCMAudio(executable='C:\\Users\\juanl\\Desktop\\ffmpeg\\bin\\ffmpeg.exe',
                               source='juan.mp3'))
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = await voice_channel.connect()
        vc.play(source)
        while vc.is_playing():  # Checks if voice is playing
            await asyncio.sleep(1)  # While it's playing it sleeps for 1 second
        else:
            await asyncio.sleep(5)  # If it's not playing it waits 15 seconds
            while vc.is_playing():  # and checks once again if the bot is not playing
                break  # if it's playing it breaks
            else:
                await vc.disconnect()  # if not it disconnects


@bot.command(name='ice')
async def ice(ctx):
    source = discord.PCMVolumeTransformer(
        discord.FFmpegPCMAudio(executable='C:\\Users\\juanl\\Desktop\\ffmpeg\\bin\\ffmpeg.exe',
                               source='ice.mp3'))
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = await voice_channel.connect()
        vc.play(source)
        while vc.is_playing():  # Checks if voice is playing
            await asyncio.sleep(1)  # While it's playing it sleeps for 1 second
        else:
            await asyncio.sleep(5)  # If it's not playing it waits 15 seconds
            while vc.is_playing():  # and checks once again if the bot is not playing
                break  # if it's playing it breaks
            else:
                await vc.disconnect()  # if not it disconnects


@bot.command(name='helpme')
async def ice(ctx):
    source = discord.PCMVolumeTransformer(
        discord.FFmpegPCMAudio(executable='C:\\Users\\juanl\\Desktop\\ffmpeg\\bin\\ffmpeg.exe',
                               source='helpme.mp3'))
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = await voice_channel.connect()
        vc.play(source)
        while vc.is_playing():  # Checks if voice is playing
            await asyncio.sleep(1)  # While it's playing it sleeps for 1 second
        else:
            await asyncio.sleep(5)  # If it's not playing it waits 15 seconds
            while vc.is_playing():  # and checks once again if the bot is not playing
                break  # if it's playing it breaks
            else:
                await vc.disconnect()  # if not it disconnects


@bot.command(name='invest')
async def ice(ctx):
    source = discord.PCMVolumeTransformer(
        discord.FFmpegPCMAudio(executable='C:\\Users\\juanl\\Desktop\\ffmpeg\\bin\\ffmpeg.exe',
                               source='game.mp3'))
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = await voice_channel.connect()
        vc.play(source)
        while vc.is_playing():  # Checks if voice is playing
            await asyncio.sleep(1)  # While it's playing it sleeps for 1 second
        else:
            await asyncio.sleep(5)  # If it's not playing it waits 15 seconds
            while vc.is_playing():  # and checks once again if the bot is not playing
                break  # if it's playing it breaks
            else:
                await vc.disconnect()  # if not it disconnects


@bot.command(name='sus')
async def ice(ctx):
    source = discord.PCMVolumeTransformer(
        discord.FFmpegPCMAudio(executable='C:\\Users\\juanl\\Desktop\\ffmpeg\\bin\\ffmpeg.exe',
                               source='sus.mp3'))
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = await voice_channel.connect()
        vc.play(source)
        while vc.is_playing():  # Checks if voice is playing
            await asyncio.sleep(1)  # While it's playing it sleeps for 1 second
        else:
            await asyncio.sleep(5)  # If it's not playing it waits 15 seconds
            while vc.is_playing():  # and checks once again if the bot is not playing
                break  # if it's playing it breaks
            else:
                await vc.disconnect()  # if not it disconnects


@bot.command(name='people')
async def ice(ctx):
    source = discord.PCMVolumeTransformer(
        discord.FFmpegPCMAudio(executable='C:\\Users\\juanl\\Desktop\\ffmpeg\\bin\\ffmpeg.exe',
                               source='women.mp3'))
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = await voice_channel.connect()
        vc.play(source)
        while vc.is_playing():  # Checks if voice is playing
            await asyncio.sleep(1)  # While it's playing it sleeps for 1 second
        else:
            await asyncio.sleep(5)  # If it's not playing it waits 15 seconds
            while vc.is_playing():  # and checks once again if the bot is not playing
                break  # if it's playing it breaks
            else:
                await vc.disconnect()  # if not it disconnects


@bot.command(name='believe', help="Carlos 1v1 me")
async def carlos(ctx):
    source = discord.PCMVolumeTransformer(
        discord.FFmpegPCMAudio(executable='C:\\Users\\juanl\\Desktop\\ffmpeg\\bin\\ffmpeg.exe',
                               source='carlos.mp3'))
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = await voice_channel.connect()
        vc.play(source)
        while vc.is_playing():  # Checks if voice is playing
            await asyncio.sleep(1)  # While it's playing it sleeps for 1 second
        else:
            await asyncio.sleep(5)  # If it's not playing it waits 15 seconds
            while vc.is_playing():  # and checks once again if the bot is not playing
                break  # if it's playing it breaks
            else:
                await vc.disconnect()  # if not it disconnects


@bot.command(name='diego')
async def pogchamp(ctx):
    source = discord.PCMVolumeTransformer(
        discord.FFmpegPCMAudio(executable='C:\\Users\\juanl\\Desktop\\ffmpeg\\bin\\ffmpeg.exe',
                               source='pogchamp.mp3'))
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = await voice_channel.connect()
        vc.play(source)
        while vc.is_playing():  # Checks if voice is playing
            await asyncio.sleep(1)  # While it's playing it sleeps for 1 second
        else:
            await asyncio.sleep(5)  # If it's not playing it waits 15 seconds
            while vc.is_playing():  # and checks once again if the bot is not playing
                break  # if it's playing it breaks
            else:
                await vc.disconnect()  # if not it disconnects


@bot.command(name='leave', help="Makes me leave the voice channel uwu")
async def leave_channel(ctx):
    print("author vc is: ")
    for vc in bot.voice_clients:
        print(vc.channel)
        if ctx.author.voice.channel == vc.channel:
            await vc.disconnect()
            await ctx.send("Left the channel, goodbye")
            return
    await ctx.send("You aren't connected to a voice channel!")


@bot.command(name='bbgirl')
async def bb(ctx):
    await ctx.send(file=discord.File('bbgirl.jpg'))


@bot.command(name='rip')
async def rip(ctx):
    await ctx.send(file=discord.File('piss.png'))


@bot.command(name='built', help="just different :KEKW:")
async def carlos(ctx):
    source = discord.PCMVolumeTransformer(
        discord.FFmpegPCMAudio(executable='C:\\Users\\juanl\\Desktop\\ffmpeg\\bin\\ffmpeg.exe',
                               source='different.mp3'), volume=0.6)
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        for v in bot.voice_clients:
            if ctx.author.voice.channel == v.channel:
                await ctx.send("I'm already in another channel! Please wait while we implement a queue for commands")
                return
        vc = await voice_channel.connect()
        vc.play(source)
        while vc.is_playing():  # Checks if voice is playing
            await asyncio.sleep(1)  # While it's playing it sleeps for 1 second
        else:
            await asyncio.sleep(5)  # If it's not playing it waits 15 seconds
            while vc.is_playing():  # and checks once again if the bot is not playing
                break  # if it's playing it breaks
            else:
                await vc.disconnect()  # if not it disconnects
    else:
        await ctx.send("You're not in a voice channel idiot")


bot.run(token)

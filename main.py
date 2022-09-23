#Se importan las librerias para el bot
import discord
import urllib.request
import json
from discord.ext import commands
import aiohttp
from datetime import datetime
import random


#Token/codigo privado para la configuracion del bot
with open('.env') as book:
    code = book.read()
    token = code.partition('=')[2].strip().strip('/')
del book, code

key = 'AIzaSyD3Ft9G0NKBKI-076jVugUUgk6t282wIfc'

client = discord.Client(intents=discord.Intents.default())

#Prefijo para los comandos del bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents) 


        
#Saludo y mensajes del bot
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Holi {member.name}, bienvenido al servidor de pruebas!'
    )

#ping-pong
@bot.command()
async def ping(ctx):
  await ctx.send('Pong!')


#marco-polo
@bot.command()
async def marco(ctx):
  await ctx.send('Polo!!')


#Ecuaciones basicas

#Codigo de texto para que el bot realice sumas
@bot.command(name = 'suma')
async def sumar(ctx, num1,num2):
    respuesta = int(num1) + int(num2)
    await ctx.send(respuesta)

#Codigo de texto para que el bot realice restas
@bot.command(name = 'resta')
async def restar(ctx, num1,num2):
    respuesta = int(num1) - int(num2)
    await ctx.send(respuesta)

    #Codigo de texto para que el bot realice division
@bot.command(name = 'divide')
async def dividir(ctx, num1,num2):
    respuesta = int(num1) / int(num2)
    await ctx.send(respuesta)

#Codigo de texto para que el bot realice multiplicaciones
@bot.command(name = 'mt')
async def multiplicar(ctx, num1,num2):
    respuesta = int(num1) * int(num2)
    await ctx.send(respuesta)


#Codigo para saber la cantidad de Subscriptores que posee algun youtuber
@bot.command(name='Subs')
async def subs(ctx, username):
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + username + "&key=" + key).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    response = username + "tiene" + "{:,d}".format(int(subs)) + " suscriptores!"
    await ctx.send(response)


#meme
@bot.command(name = 'meme')
async def meme(ctx):
    async with aiohttp.ClientSession() as session:
        x = 'https://www.reddit.com/r/SinhalaMemes/new.json?sort=hot'
        async with session.get(x) as resp:
            memes = await resp.json()
            
            y = random.randint(0,25)
            print(y)

            embed = discord.Embed(
                title = 'NES Sinhala Memes',
                color= 0x00ff7f,
                description= memes["data"]["children"][y]['data']['title'],
                timestamp=datetime.utcnow()
            )

            embed.set_image(url = memes["data"]["children"][y]['data']['url'])
            await ctx.send(embed=embed)

@bot.command(name='ememe')
async def meme(ctx):
    async with aiohttp.ClientSession() as session:
        x = 'https://www.reddit.com/r/memes/new.json?sort=hot'
        async with session.get(x) as resp:
            memes = await resp.json()
            
            y = random.randint(0,25)
            print(y)

            embed = discord.Embed(
                title = 'NES Sinhala Memes',
                color= 0x00ff7f,
                description= memes["data"]["children"][y]['data']['title'],
                timestamp=datetime.utcnow()
            )

            embed.set_image(url = memes["data"]["children"][y]['data']['url'])
            await ctx.send(embed=embed)

@bot.command(name='valo')
async def meme(ctx):
    async with aiohttp.ClientSession() as session:
        x = 'https://www.reddit.com/r/ValorantMemes/new.json?sort=hot'
        async with session.get(x) as resp:
            memes = await resp.json()
            
            y = random.randint(0,50)
            print(y)

            embed = discord.Embed(
                title = 'NES Sinhala Memes',
                color= 0x00ff7f,
                description= memes["data"]["children"][y]['data']['title'],
                timestamp=datetime.utcnow()
            )

            embed.set_image(url = memes["data"]["children"][y]['data']['url'])
            await ctx.send(embed=embed)



bot.run('MTAyMDQ2MzUyNDk4OTkxNTIxOA.GXJ5zx.ZHlnrdHe-6Vl6bLPXCLB1ffF_ifp29WeDApCf8')




import discord
import random, os, requests
from discord.ext import commands
from Conta_bot import mina
from Conta_bot import cion
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$¿Cuales son las consequencias de la contaminación?'):    
        await message.channel.send("La contaminación ambiental tiene graves consecuencias para la salud de las personas y para el medio ambiente.Deforestación 🌲Pesticidas y otros químicos 🧪")
    elif message.content.startswith('$¿Cómo afecta el reciclaje al medio ambiente?'):
        await message.channel.send("El reciclaje reduce la necesidad de extraer nuevos recursos naturales, lo que minimiza el impacto ambiental de la minería, la tala de árboles y la producción de nuevos materiales.")
    elif message.content.startswith('$¿Qué materiales se pueden reciclar?'):
        await message.channel.send("Se pueden reciclar materiales como el vidrio, el papel, el cartón, los plásticos y algunos metales, dependiendo del sistema de reciclaje local.")        
    elif message.content.startswith('$¿Cual es el impacto del reciclaje en la vida?'):
        await message.channel.send("El reciclaje tiene un impacto positivo en la vida de las personas y el medio ambiente, ya que ayuda a reducir la contaminación, conservar recursos naturales y crear comunidades más sostenibles.")
    elif message.content.startswith('$¿Es cierto que reciclar cuesta más que producir nuevos productos?'):
        await message.channel.send("Aunque el reciclaje puede tener un costo inicial, a largo plazo es más económico porque reduce la necesidad de recursos nuevos y ayuda a prevenir problemas ambientales costosos.")
    elif message.content.startswith("$Quien eres?"):
        await message.channel.send(mina(1))
    elif message.content.startswith("$Que haces?"):
        await message.channel.send(cion(1))
    else:
        await message.channel.send(message.content)

client.run("MT8")

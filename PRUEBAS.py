#Template para que usen con la clase BOT! 

#Importando librerías (se modifica al gusto)

import discord
import requests  #Asegúrese de que tiene instalada la biblioteca requests. Si no es así, ¡instálala con pip install!
from discord.ext import commands
import os
import random

#NO BORRAR 
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()

# Activar el privilegio de lectura de mensajes
intents.message_content = True

# Crear un bot en la variable cliente y transferirle los privilegios, también se define que el bot funcione con ! 
bot = commands.Bot(command_prefix='!', intents=intents) 

consejos = ["Pon la basura en su lugar",
    "No uses el carro si no es necesario",
    "Planta un árbol",
    "Maneja menos",
    "Reusa",
    "Recicla",
    "Apoya a tu comunidad"]


citas = ["Hola, ¿eres el Sol? porque me derretí cuando te vi.",
    "Debió haberte dolido caer desde el cielo, porque eres la estrella más brillante",
    "No sabía que la perfección tuviera un rostro, hasta que vi el tuyo",
    "¿A dónde tan guapo?"]


babosadas = ["Yo podré ser un bot, pero tu simplemente no sabes pensar originalmente",
    "Si no quieres hablar luego no te preguntes por qué ella no te habla",
    "Algún día me pregunto si es de verdad tonto o sólo se hace...",
    "Ya ni yoooooo" ]



@bot.event
async def on_ready():
    print(f"Hemos iniciado sesión como {bot.user}")


#Así se hacen los comandos para que el bot opere
@bot.command()  
async def Consejos(ctx):   #De aquí depende el comando, el nombre que se pone aquí es el comando que el bot usará (!Micomando)
    #AQUÍ VA EL FUNCIONAMIENTO DEL BOT, dependiendo de lo que quieran que haga    
    await ctx.send(random.choice(consejos))  #acá es lo que el BOT va a responderte cuando escribas !Micomando

@bot.command()
async def UwU(ctx):
    await ctx.send(random.choice(citas))

@bot.command()
async def HEY(ctx):
    await ctx.send(random.choice(babosadas))

bot.run("MTE2NDcyMDY2MzM0OTcwNjc1Mw.G1QM43.lPbbjGwUkzv5wbGLfFJMx6v-60iGRpwhpRhD9M")

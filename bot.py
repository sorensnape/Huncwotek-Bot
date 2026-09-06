import discord
from discord.ext import commands
import random
import os
from flask import Flask
from threading import Thread

# --- SERWER WWW DO "BUDZENIA" BOTA ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run_server():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_server)
    t.start()
# --------------------------------------

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def uratujucz(ctx):
    odpowiedzi = [
        "*Lecisz już na hipogryfie, niestety lądujesz w złej części Azkabanu i łapią Cię dementorzy.* **Otrzymujesz 5 punktów - za dobre chęci.**",
        "*Przylatuje po Ciebie hipogryf, wsiadasz na niego i lecisz do Azkabanu.* **Otrzymujesz 10 punktów!**"
    ]
    await ctx.send(random.choice(odpowiedzi))

@bot.command()
async def uratujprof(ctx):
    odpowiedzi = [
        "*Lecisz już na hipogryfie, niestety lądujesz w złej części Azkabanu i łapią Cię dementorzy.* **Otrzymujesz 3 punkty - za dobre chęci.**",
        "*Przylatuje po Ciebie hipogryf, wsiadasz na niego i lecisz do Azkabanu.* **Otrzymujesz 6 punktów!**"
    ]
    await ctx.send(random.choice(odpowiedzi))

@bot.command()
async def labirynt(ctx):
    await ctx.send("*[Podbiega szybko i staje obok, wręczając Ci po cichu kawałek [pergaminu](https://jpcdn.it/img/small/0257f36212dfda8b8060cfd9d6464de3.webp)].* **Oto dzisiejszy labirynt! Nie zapomnij tylko odesłać wypełnionego poprzez formularz!** *[Podaje mu następny [pergamin](https://tiny.pl/dx98w) i zadowolony wraca do swojej wcześniejszej zabawy.]*")

@bot.command()
async def zagadka(ctx):
    await ctx.send("*[Podbiega szybko i staje przed tobą, kaszląc dwa razy.]* ***Czekasz na zagadkę? No dobrze… Oto dzisiejsza!***\n`Zawsze nosi kolorowe szaty, uwielbia słodycze i jest uważany za najpotężniejszego czarodzieja swoich czasów. To właśnie on przez lata kierował Hogwartem i opiekował się Harrym. Kto to taki?`\n***Nie zapomnij o odpowiedzi! Masz tu jeszcze formularz na to.*** *[Podaje szybko części [pergaminu](https://tiny.pl/dxp66)].*")

# Uruchomienie "budzika"
keep_alive()

# Start bota
bot.run(os.environ['TOKEN'])

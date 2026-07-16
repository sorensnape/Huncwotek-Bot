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
async def uratuj(ctx):
    odpowiedzi = [
        "*Lecisz już na hipogryfie, niestety lądujesz w złej części Azkabanu i łapią Cię dementorzy.* **Otrzymujesz 5 punktów - za dobre chęci.**",
        "*Przylatuje po Ciebie hipogryf, wsiadasz na niego i lecisz do Azkabanu.* **Otrzymujesz 10 punktów!**"
    ]
    await ctx.send(random.choice(odpowiedzi))

@bot.command()
async def labirynt(ctx):
    await ctx.send("*Podbiega do Ciebie i staje obok, wręczając Ci po cichu kawałek [pergaminu](LINK_DO_LABIRYNTU).* **Oto dzisiejszy labirynt! Nie zapomnij tylko odesłać wypełnionego poprzez formularz!** *Podaje mu następny [pergamin](https://tiny.pl/dx98w) i zadowolony wraca do swojej wcześniejszej zabawy.*")

@bot.command()
async def zagadka(ctx):
    await ctx.send("*[Podbiega do ciebie i staje przed tobą, kaszląc dwa razy.]* ***Czekasz na zagadkę? No dobrze… Oto dzisiejsza!***\nTwoja zagadka tutaj.\n***Nie zapomnij o odpowiedzi! Masz tu jeszcze formularz na to.*** *[Podaje szybko części [pergaminu](https://tiny.pl/dxp66)].*")

# Uruchomienie "budzika"
keep_alive()

# Start bota
bot.run(os.environ['TOKEN'])

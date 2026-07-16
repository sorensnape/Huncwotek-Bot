import discord
from discord.ext import commands
import random

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

bot.run(os.environ['TOKEN'])
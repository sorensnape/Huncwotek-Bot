import discord
from discord.ext import commands
import random
import os

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
    await ctx.send("*[Podbiega szybko i staje obok, wręczając Ci po cichu kawałek [pergaminu](https://jpcdn.it/img/small/633d0289ccf2dc00e95f397f97a36d0f.webp)].* **Oto dzisiejszy labirynt! Nie zapomnij tylko odesłać wypełnionego poprzez formularz!** *[Podaje mu następny [pergamin](https://tiny.pl/dx98w) i zadowolony wraca do swojej wcześniejszej zabawy.]*")

@bot.command()
async def zagadka(ctx):
    await ctx.send("*[Podbiega szybko i staje przed tobą, kaszląc dwa razy.]* ***Czekasz na zagadkę? No dobrze… Oto dzisiejsza!***\n`Harry nosi ją od dziecka jako wspomnienie nocy, w której stracił rodziców. To wyjątkowy znak, który łączy go na zawsze z mrocznym panem i sprawia, że jest rozpoznawalny dla każdego w świecie magii. Co to za ślad?`\n***Nie zapomnij o odpowiedzi! Masz tu jeszcze formularz na to.*** *[Podaje szybko części [pergaminu](https://tiny.pl/dxp66)].*")

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}!')

bot.run(os.environ['TOKEN'])

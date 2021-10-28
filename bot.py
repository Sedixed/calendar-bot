from calendar import get_calendars
import os
import discord
from discord.ext import commands
from datetime import datetime
from dotenv import load_dotenv
import asyncio
from PIL import Image
from PIL import ImageChops

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.typing = True
bot = commands.Bot(command_prefix='-', intents=intents)


@bot.event
async def on_ready():
    await send_calendars()

licences = ("2", "3")
td_ids = (["1", 881189193668231168],
          ["2", 881189307812032522],
          ["3", 881189344860311634],
          ["4", 881189370911162389],
          ["1", 884101420436037652],
          ["2", 884104067952037928],
          ["3", 884104121135816804],
          ["sd", 884104193428820038])

async def send_calendars():
    while True:
        now = datetime.now()
        h = now.strftime("%H")
        m = now.strftime("%M")
        s = now.strftime("%S")
        if (h == 20 and m == 0 and s == 0) or (h == 8 and m == 0 and s == 0):
            get_calendars()
            for l in licences:
                for td in td_ids:
                    img = Image.open(f"l{l}td{td[0]}.png", 'r')
                    channel = bot.get_channel(td[1])

                    last_sent = await channel.fetch_message(channel.last_message_id)

                    if last_sent is None:
                        await channel.send(file=discord.File(img))

                    elif last_sent.attachment:
                        actual = Image.open(last_sent.attachments[0].url, 'r')
                        diff = ImageChops.difference(img, actual)

                        if diff.getbbox():
                            last_sent.delete()
                            await channel.send(file=discord.File(img))


        #print(f"{d} : {h}:{m}:{s}")
        #await asyncio.sleep(1)

# --- Commands ---

@bot.command(name="calendar")
async def private_calendar(ctx, licence: int, td: int):
    img = Image.open("l{licence}td{td}.png", 'r')

# --- Launch ---

bot.run(TOKEN)
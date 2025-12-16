import discord
from discord.ext import commands
import os
import random
from PIL import Image

TOKEN = "MTQ1MDM1MzEwMjIyMDgyNDY1Nw.GEQuYo.aIfqFy44SNbpLV0BIT6RTusn1jkEggMF2V42_c"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

IMAGE_FOLDER = "."

MESSAGES = [
    "Oh eto na! Iiyak kana e 😏",
    "Hi Bestie! Charot Reading time na 💅",
    "Ikaw nanaman?! Sige, basa tayo 🤪",
    "Tahimik lang… eto na ang sagot mo 👀",
    "Ay hala siya… Charot Reading incoming 🔮"
]

# 🃏 ALL 31 IMAGES WITH MEANINGS
IMAGE_MEANINGS = {
    "charot (1).jpg": "masarap",
    "charot (2).jpg": "very good ka sa ginagawa mo ngayon",
    "charot (3).jpg": "wag mo na uulitin",
    "charot (4).jpg": "sobrang bata pa, nak!",
    "charot (5).jpg": "oh pakak!",
    "charot (6).jpg": "AGHHHH!!!",
    "charot (7).jpg": "BUT WAIT!",
    "charot (8).jpg": "Eto na ang iniintay mo!",
    "charot (9).jpg": "palaban",
    "charot (10).jpg": "ayoko na marinig pa!",
    "charot (11).jpg": "TEKA! OKAY, GO!",
    "charot (12).jpg": "EKALAL",
    "charot (13).jpg": "INIS",
    "charot (14).jpg": "hihihi",
    "charot (15).jpg": "your soulmate is coming",
    "charot (16).jpg": "blaming yourself",
    "charot (17).jpg": "SHOCKED",
    "charot (18).jpg": "bantot",
    "charot (19).jpg": "YES!",
    "charot (20).jpg": "It's up to you, te.",
    "charot (21).jpg": "Go for it!",
    "charot (22).jpg": "Hopeless",
    "charot (23).jpg": "Burnout",
    "charot (24).jpg": "STOP",
    "charot (25).jpg": "Contemplating",
    "charot (26).jpg": "May iba siya",
    "charot (27).jpg": "Don't change yourself for someone",
    "charot (28).jpg": "GALIT NA GALIT",
    "charot (29).jpg": "Magkakaroon ka rin",
    "charot (30).jpg": "Ang mga pipiliin mong desisyon sa buhay",
    "charot (31).jpg": "About to crashout"
}

# 🖼️ MERGE IMAGES HORIZONTALLY (SMALLER)
def merge_images(image_paths, height=280):
    images = [Image.open(p) for p in image_paths]
    resized = []

    for img in images:
        ratio = height / img.height
        resized.append(img.resize((int(img.width * ratio), height)))

    total_width = sum(img.width for img in resized)
    combined = Image.new("RGB", (total_width + 20, height + 20), "#f5f5f5")

    x = 10
    for img in resized:
        combined.paste(img, (x, 10))
        x += img.width

    output = "charot_reading.jpg"
    combined.save(output)
    return output

@bot.event
async def on_ready():
    print("✨ Charot Bot is online!")

@bot.command()
async def charot(ctx, arg=None):
    if arg != "reading":
        return

    cards = list(IMAGE_MEANINGS.keys())
    selected = random.sample(cards, 5)

    await ctx.send(random.choice(MESSAGES))

    reading = ""
    for i, card in enumerate(selected, start=1):
        reading += f"**Card {i}:** {IMAGE_MEANINGS[card]}\n"

    image_paths = [os.path.join(IMAGE_FOLDER, c) for c in selected]
    merged_image = merge_images(image_paths)

    file = discord.File(merged_image, filename="charot_reading.jpg")
    embed = discord.Embed(
        title="✨ Your Charot Reading ✨",
        description=reading
    )
    embed.set_image(url="attachment://charot_reading.jpg")

    await ctx.send(embed=embed, file=file)

bot.run(TOKEN)

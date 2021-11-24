import discord
import requests
import json
import random
import os
from replit import db

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "depressing", "breakup", "angry", "hotas", "suicide", "suicidal"]

starter_encouragement = [
  "Daddy chill !!!",
  "cheer up !",
  "Weird flex but ok",
  "O pita dong",
  "প্যারা নাই চিল!"
]


def get_quote():
    resp = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(resp.text)
    quote = json_data[0]['q'] + "-" + json_data[0]["a"]
    return quote

def update_data(name, data1):
  if name in db.keys():
    name = db[name]
    name = str(name) + (data1)
    db[name] = name
  else:
    db[name] = [data1]


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    print(message.author.name)
    if message.author == client.user:
        return
    msg = message.content

    if message.content.startswith('$sup'):
        await message.channel.send("chillin")

    elif message.content.startswith('$poipoi'):
        await message.channel.send("পই পই করে হিসাব রাখতে হবে!")

    elif message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    elif any(word in msg for word in sad_words):
         await message.channel.send(random.choice(starter_encouragement))

    elif msg.startswith("$poinote"):
      name = str(message.author.name)
      data1 = msg.split("$poinote",1)[1]
      update_data(name,data1)
      await message.channel.send("New PoiPoi note added.")
    
    elif msg.startswith("$poishow"):
      name = str(message.author.name)
      await message.channel.send(db[name])

    elif message.content.startswith('$xd'):
        await message.channel.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

 
client.run(os.environ['token']) # discord bot token 



import discord
import os
import requests
import json
import random
from replit import db


client = discord.Client()

sad_words = ["traurig","enttäuscht","unglücklich","miserabel","deprimierend","sad", "unhappy","wütend","depressed"]

starter_cheers = ["Du schaffst das!","Du bist eine tolle Person!","Ich mag dich!"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_cheers(cheering_message):
  if "cheers" in db.keys():
    cheers = db["cheers"]
    cheers.append(cheering_message)
    db["cheers"] = cheers
  else:
    db["cheers"] = [cheering_message]

def delete_cheer(index):
  cheers = db["cheers"]
  if len(cheers)> index:
    del cheers[index]
    db["cheers"] = cheers

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$Zitat'):
    quote = get_quote()
    await message.channel.send(quote)

  options = starter_cheers
  if "cheers" in db.keys():
    options = options + db["cheers"]

  
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(options))
  
  if msg.startswith('$new'):
    cheering_message = msg.split("$new ",1)[1]
    update_cheers(cheering_message)
    await message.channel.send("Neue Nachricht hinzugefügt.")

  if msg.startswith("$del"):
    cheers = []
    if "cheers" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_cheer(index)
      cheers = db["cheers"]
    await message.channel.send(cheers)

client.run(os.getenv('TOKEN'))

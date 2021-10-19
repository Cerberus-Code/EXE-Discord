
import discord
import os
import scripts.mongo as mongo
from discord.ext import commands

# Define Intents
intents = discord.Intents.default()

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
  loaded = []
  unloaded = []
  print(f'Connected at - {client.user}\n')
  for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        loaded.append(filename[:-3])
      else:
        unloaded.append(filename[:-3])
  print(f'{"-"*25}')
  for cog in loaded:
    print(f'Successfully loaded {cog}')
  print(f'{"-"*25}\n')
  print(f'{"-"*25}')
  for cog in unloaded:
    print(f'Unable to load {cog}')
  print(f'{"-"*25}')

client.run(os.environ['token'])

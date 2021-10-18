
from discord.ext import commands

class Temporary(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def ping(self, ctx, *, args):
    await ctx.send(args)

def setup(client):
  client.add_cog(Temporary(client))

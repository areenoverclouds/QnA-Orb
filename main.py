import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='?')

@client.event
async def on_ready():
  print("Bot is ready.")

@client.command()
async def Help(ctx):
  await ctx.send(f'Welcome to The QnA Orb Bot! \nUse prefix ? \nUse command ?ping to play ping pong, jk it only tells your ping. \nUse command ?ama (your question) to ask any yes/no question to the tarot guru! \nUse command ?eg for examples of questions you can ask!')

@client.command()
async def eg(ctx):
  await ctx.send(f'Try asking : ?ama Will I get a new pet this year?')

@client.command()
async def ping(ctx):
  await ctx.send(f'Your ping is {round(client.latency*1000)}ms.')

@client.command()
async def ama(ctx,*,question):
  responses = ["Hmm maybe.", 
                "Keep your hopes high!", 
                "Absolutely!",
                "Without a doubt.",
                "I doubt that!",
                "My reply is a no.",
                "Don't count on it.",
                "The universe says yes!",
                "The stars are in your favour.",
                "Follow Venus and you will.",
                "Certainly!",
                "Most likely, yes.",
                "Pretty much.",
                "Reply hazy, try again.",
                "Can't be sure",
                "Might be possible.",
                "I don't think so.",
                "For sure.",
                "I'm afraid, no.",
                "The universe says no.",
                "Not clear.",
                "I believe, yes.",
                "That may be possible."]
  await ctx.send(f'Your question: {question} \nCrystal Orb says: {random.choice(responses)}')


client.run('ODYwMDQzOTA5MzAzNzYyOTU1.YN1gTg.yqfiHlrXECLzydWqpEiOMBrTbT4')





import os 
import discord
from dotenv import load_dotenv

#Lade die .env Datei
load_dotenv()

bot = discord.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is ready")

#Erstelle einen command der den Bot zum joinen eines Voicechannels bringt
@bot.command()
async def join(ctx, channel: discord.VoiceChannel):
    await channel.connect()
    await ctx.respond('Ich bin jetzt im Channel')

#Erstelle einen command der ein Soundfile abspielt
@bot.command()
async def play(ctx):
    voice_client:discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    audio_source = discord.FFmpegPCMAudio(r"Sounds\UWU.mp3")
    voice_client.play(audio_source)
    await ctx.respond('Ich spiele jetzt ein Soundfile')

#erstelle einen command der den Bot aus dem Voicechannel kickt
@bot.command()
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    await voice.disconnect()
    await ctx.respond('Ich habe den Channel verlassen')

bot.run(os.getenv('BOT_TOKEN'))
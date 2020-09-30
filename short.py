import discord

client = discord.Client()

@client.event
async def on_ready():
    print("ログインドーン!")

@client.event
async def on_message(message):
    if message.content.startswith('!sc'):
        rep = str(message.content)
        rep = rep.replace('!sc','!soundcloud',1)
        await message.author.voice.channel.connect()
        await message.channel.send(rep)
        await message.author.guild.voice_client.disconnect()
        

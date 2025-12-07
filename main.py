import os
import discord
from discord.ext import commands

# Create bot instance with intents
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    # Don't respond to ourselves
    if message.author == bot.user:
        return
    
    # Check if the message is "ゆーまおさん"
    if message.content == 'ゆーまおさん':
        await message.channel.send('ゆーまおだよ')
    
    # Process commands
    await bot.process_commands(message)

def main():
    # Get token from environment variable
    token = os.getenv('DISCORD_BOT_TOKEN')
    if not token:
        print('Error: DISCORD_BOT_TOKEN environment variable is not set')
        print('Please set it with: export DISCORD_BOT_TOKEN=your_token_here')
        return
    
    bot.run(token)

if __name__ == "__main__":
    main()

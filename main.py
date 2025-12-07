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
    
    # Check if the message is "ゆーまおさん" (strip whitespace)
    if message.content.strip() == 'ゆーまおさん':
        await message.channel.send('ゆーまおだよ')
    
    # Process commands
    await bot.process_commands(message)

def main():
    # Get token from environment variable
    token = os.getenv('DISCORD_BOT_TOKEN')
    if not token:
        raise ValueError(
            'DISCORD_BOT_TOKEN environment variable is not set.\n'
            'Please set it with: export DISCORD_BOT_TOKEN=your_token_here'
        )
    
    try:
        bot.run(token)
    except discord.LoginFailure:
        print('Error: Invalid Discord Bot Token')
        print('Please check your token in the Discord Developer Portal')
        raise
    except Exception as e:
        print(f'Error: Failed to run bot: {e}')
        raise

if __name__ == "__main__":
    main()

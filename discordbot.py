from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix=';')
token = os.environ['DBT']


@bot.event
async def on_message(message):
    try:
        if message.author.bot:
            return
        await bot.process_commands(message)
    except Exception:
        await message.channel.send(f'```\n{traceback.format_exc()}\n```')


@bot.commands
async def sss(ctx):
    await ctx.send('test')


bot.run(token)

import discord
import asyncio
import random
from discord.ext import commands
from sett_tok import BOT_TOKEN 

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.event
async def on_message(message):
        if message.content.startswith('!гойда'):
            msg = await message.channel.send('Здесь же чёрным по белому написано!')
            await asyncio.sleep(3.0)
            await msg.edit(content='ГООООООООООООООООООООООЙДА!')

@bot.event
async def on_message_edit(before, after):
    msg = f'**{before.author}** edited their message:\n{before.content} -> {after.content}'
    await before.channel.send(msg)

@bot.event
async def on_message(message):
        if message.author == bot.user:
            return

        if message.content.startswith('!угадай число'):
            await message.channel.send('Угадай число от 1 до 10')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await bot.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Время вышло, к сожалению вы не успели). Правильный ответ - {answer}.')

            if int(guess.content) == answer:
                await message.channel.send('Воу, ты угадал!')
            else:
                await message.channel.send(f'К сожалению ты не угадал, правильный ответ - {answer}.')

bot.run(BOT_TOKEN)
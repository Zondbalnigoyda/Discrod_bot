import discord
import asyncio
import random
from datetime import datetime
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

#Создать квиз не получилось из-за трудностей возникших в процессе реализации.

@bot.event
async def on_message(message):
    if message.content.startswith('!кубик'):
        await message.channel.send('Подбрасываю кубик...')
        await asyncio.sleep(3.0)
        kub_num = random.randint(1,6)
        if kub_num == 1:
            await message.channel.send('Выпало число 1')
        elif kub_num == 2:
            await message.channel.send('Выпало число 2')
        elif kub_num == 3:
            await message.channel.send('Выпало число 3')
        elif kub_num == 4:
            await message.channel.send('Выпало число 4')
        elif kub_num == 5:
            await message.channel.send('Выпало число 5')
        elif kub_num == 6:
            await message.channel.send('Выпало число 6')

@bot.event
async def on_message(message):
    if message.content.startswith('!help') or message.content.startswith('!помощь') or message.content.startswith('!команды') or message.content.startswith('!comands'):
        await message.channel.send('-------------------------СПИСОК ДОСТУПНЫХ КОМАНД-------------------------------')
        await message.channel.send('============================================================================')
        await message.channel.send('=1.=$hello - при вводе бот скажет вам привет====================================')
        await message.channel.send('=2.=#he - при вводе бот напишет hehehehehe===================================')    
        await message.channel.send('=3.=!гойда, при вводе бот напишет сообщение, а потом его отредактирует=========')    
        await message.channel.send('=4.=!угадай число, при вводе вы должны будете угадать число за пять секунд=====')     
        await message.channel.send('=5.=!кубик, число при вводе бот подбросит кубик и напишет вам результат========')    
        await message.channel.send('============================================================================')
        await message.channel.send('--------------------------------------------------------------------------------------------')    

bot.run(BOT_TOKEN)

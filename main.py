import time
import discord
import datetime
from random import choice
from discord.ext import commands

TOKEN = 'put_token_here' # TODO: put token
CHANEL_ID, ROLE_ID, thread = None, None, None

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

messages = ('Гоу ту ворк', 'Работать', 'Работать быстро', 'Гоу ту ворк нигасес')


async def mainloop():
    while True:
        if datetime.datetime.now().hour not in range(10, 16):
            msg = f'''{bot.get_channel(CHANEL_ID).guild.get_role(ROLE_ID).mention} \n\n {choice(messages)}'''
            await bot.get_channel(CHANEL_ID).send(msg)
            time.sleep(25 * 60)


@bot.command(name='init_me')
async def init_go_work(ctx, role: discord.Role):
    global CHANEL_ID, ROLE_ID, thread
    if not CHANEL_ID:
        CHANEL_ID = discord.utils.get(bot.get_all_channels(), name='🤓новости-для-администрации').id

    if not ROLE_ID:
        ROLE_ID = role.id

    for emoji in ctx.guild.emojis:
        print(emoji.name, emoji.id)

    await ctx.reply('Оке')
    await mainloop()


bot.run(TOKEN)

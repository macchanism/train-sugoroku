import discord
from discord.ext import commands
from discord.commands import Option
import random
import config
import tool
import railroad


# Initial Process
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def cmd(
    ctx,
    crrsta: Option(str, 'Current Station?'),
    line: Option(str, 'Line?', choices=railroad.env.railroad_list),
    bound: Option(str, 'Bound for?', choices=railroad.env.bound_list),
):
    # crrsta, line, boundに整合性があるか
    if not railroad.railroad_tool.is_station_in_line(crrsta, line):
        await ctx.respond(f'Error!')
        return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    s = railroad.railroad_tool.next_stop(crrsta, line, bound, i)
    if s == -1:
        await ctx.respond(f'Error!')
        return
    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Line: {line}, Bound: {bound}, Step: {i}, Next Stop: {s}')


bot.run(config.TOKEN)

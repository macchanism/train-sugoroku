from secrets import choice
import discord
from discord.ext import commands
from discord.commands import Option
import sys
import config
import tool
import railroad

HOLIDAY = False
WALK = True

# Option
args = sys.argv
if len(args) > 3:
    exit(print("Too many arguments! Exit!"))
for a in args:
    if a == "-w" or a == "--walk":
        WALK = True
    elif a == "-nw" or a == "--notwalk":
        WALK = False
    elif a == "-h" or a == "--holiday":
        HOLIDAY = True
    elif a == "-nh" or a == "--notholiday":
        HOLIDAY = False

# Initial Process
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)


# Maintenance
@bot.slash_command(guild_ids=config.SERVER_IDs)
async def change_value(
    ctx,
    pswd: Option(str, 'PSWD?'),
    newvalue: Option(str, 'T/F?', choices=["True", "False"])
):
    if pswd != config.PSWD:
        await ctx.respond(f'**Incorrect PSWD...**')
        return

    global WALK
    if newvalue == "True":
        WALK = True
    else:
        WALK = False

    # 出力
    await ctx.respond(f'**WALK is {WALK}**')


# Slash Command
@bot.slash_command(guild_ids=config.SERVER_IDs)
async def ja(
    ctx,
    crrsta: Option(str, 'Current Station?', choices=railroad.ja.station_list),
    typ: Option(str, 'Which type?', choices=railroad.ja.type_list),
    bound: Option(str, 'Bound for?', choices=railroad.ja.bound_list)
):
    # crrsta, line, boundに整合性があるか
    if not railroad.ja.has_alignment(crrsta, typ):
        await ctx.respond(f'Error! There is not {crrsta} in this line!')
        return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = railroad.ja.next_station(crrsta, typ, bound, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # コメント
    cmnt = ""
    if nxtsta == crrsta:
        cmnt = "Stay here... Re-choose another train and retry!"
    if cmnt != "":
        cmnt = "\nComment> " + cmnt

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Type: {typ}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**'+cmnt)


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def jb(
    ctx,
    crrsta: Option(str, 'Current Station?', choices=railroad.jb.station_list),
    bound: Option(str, 'Bound for?', choices=railroad.jb.bound_list)
):
    # crrsta, line, boundに整合性があるか
    if not railroad.jb.has_alignment(crrsta):
        await ctx.respond(f'Error! There is not {crrsta} in this line!.')
        return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = railroad.jb.next_station(crrsta, bound, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # コメント
    cmnt = ""
    if nxtsta == crrsta:
        cmnt = "Stay here... Re-choose another train and retry!"
    if cmnt != "":
        cmnt = "\nComment> " + cmnt

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**'+cmnt)


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def jc(
    ctx,
    crrsta: Option(str, 'Current Station?', choices=railroad.jc.station_list),
    typ: Option(str, 'Which type?', choices=railroad.jc.type_list),
    bound: Option(str, 'Bound for?', choices=railroad.jc.bound_list)
):
    global HOLIDAY

    # crrsta, line, boundに整合性があるか
    if not railroad.jc.has_alignment(crrsta, typ, HOLIDAY):
        await ctx.respond(f'Error! There is not {crrsta} in this line!')
        return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = railroad.jc.next_station(crrsta, typ, bound, i, HOLIDAY)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # コメント
    cmnt = ""
    if nxtsta == crrsta:
        cmnt = "Stay here... Re-choose another train and retry!"
    if cmnt != "":
        cmnt = "\nComment> " + cmnt

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Type: {typ}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**'+cmnt)


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def je(
    ctx,
    crrsta: Option(str, 'Current Station?', choices=railroad.je.station_list),
    typ: Option(str, 'Which type?', choices=railroad.je.type_list),
    bound: Option(str, 'Bound for?', choices=railroad.je.bound_list)
):
    # crrsta, line, boundに整合性があるか
    if not railroad.je.has_alignment(crrsta, typ):
        await ctx.respond(f'Error! There is not {crrsta} in this line!.')
        return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = railroad.je.next_station(crrsta, typ, bound, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # WALK
    global WALK
    if WALK:
        if i in [4, 5]:
            nxtsta = railroad.je.next_station(crrsta, "各駅停車", bound, 1)
            if nxtsta == -1:
                await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
                return
            nxtsta = "WALK TO " + nxtsta + "!"
    if nxtsta == "葛西臨海公園":
        WALK = False

    # コメント
    cmnt = ""
    if nxtsta == "葛西臨海公園":
        cmnt = "Goal!!!"
    elif nxtsta == "WALK TO 葛西臨海公園!":
        cmnt = "Goal!!!"
    elif nxtsta == crrsta:
        cmnt = "Stay here... Re-choose another train and retry!"
    if cmnt != "":
        cmnt = "\nComment> " + cmnt

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Type: {typ}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**'+cmnt)


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def jj(
    ctx,
    crrsta: Option(str, 'Current Station?', choices=railroad.jj.station_list),
    typ: Option(str, 'Which type?', choices=railroad.jj.type_list),
    bound: Option(str, 'Bound for?', choices=railroad.jj.bound_list)
):
    # crrsta, line, boundに整合性があるか
    if not railroad.jj.has_alignment(crrsta, typ):
        await ctx.respond(f'Error! There is not {crrsta} in this line!')
        return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = railroad.jj.next_station(crrsta, typ, bound, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # コメント
    cmnt = ""
    if nxtsta == crrsta:
        cmnt = "Stay here... Re-choose another train and retry!"
    if cmnt != "":
        cmnt = "\nComment> " + cmnt

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Type: {typ}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**'+cmnt)


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def jk(
    ctx,
    crrsta: Option(str, 'Current Station?', choices=railroad.jk.station_list),
    typ: Option(str, 'Which type?', choices=railroad.jk.type_list),
    bound: Option(str, 'Bound for?', choices=railroad.jk.bound_list)
):
    global HOLIDAY

    # crrsta, line, boundに整合性があるか
    if not railroad.jk.has_alignment(crrsta, typ, HOLIDAY):
        await ctx.respond(f'Error! There is not {crrsta} in this line!')
        return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = railroad.jk.next_station(crrsta, typ, bound, i, HOLIDAY)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # コメント
    cmnt = ""
    if nxtsta == crrsta:
        cmnt = "Stay here... Re-choose another train and retry!"
    if cmnt != "":
        cmnt = "\nComment> " + cmnt

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Type: {typ}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**'+cmnt)


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def jl(
    ctx,
    crrsta: Option(str, 'Current Station?', choices=railroad.jl.station_list),
    bound: Option(str, 'Bound for?', choices=railroad.jl.bound_list)
):
    # crrsta, line, boundに整合性があるか
    if not railroad.jl.has_alignment(crrsta):
        await ctx.respond(f'Error! There is not {crrsta} in this line!.')
        return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = railroad.jl.next_station(crrsta, bound, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # コメント
    cmnt = ""
    if nxtsta == crrsta:
        cmnt = "Stay here... Re-choose another train and retry!"
    if cmnt != "":
        cmnt = "\nComment> " + cmnt

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**'+cmnt)


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def jo(
    ctx,
    crrsta: Option(str, 'Current Station?', choices=railroad.jo.station_list),
    bound: Option(str, 'Bound for?', choices=railroad.jo.bound_list)
):
    # crrsta, line, boundに整合性があるか
    if not railroad.jo.has_alignment(crrsta):
        await ctx.respond(f'Error! There is not {crrsta} in this line!.')
        return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = railroad.jo.next_station(crrsta, bound, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # コメント
    cmnt = ""
    if nxtsta == crrsta:
        cmnt = "Stay here... Re-choose another train and retry!"
    if cmnt != "":
        cmnt = "\nComment> " + cmnt

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**'+cmnt)


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def js(
    ctx,
    crrsta: Option(str, 'Current Station?', choices=railroad.js.station_list),
    typ: Option(str, 'Which type?', choices=railroad.js.type_list),
    bound: Option(str, 'Bound for?', choices=railroad.js.bound_list)
):
    # crrsta, line, boundに整合性があるか
    if not railroad.js.has_alignment(crrsta, typ):
        await ctx.respond(f'Error! There is not {crrsta} in this line!')
        return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = railroad.js.next_station(crrsta, typ, bound, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # コメント
    cmnt = ""
    if nxtsta == crrsta:
        cmnt = "Stay here... Re-choose another train and retry!"
    if cmnt != "":
        cmnt = "\nComment> " + cmnt

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Type: {typ}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**'+cmnt)


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def jt(
    ctx,
    crrsta: Option(str, 'Current Station?', choices=railroad.jt.station_list),
    typ: Option(str, 'Which type?', choices=railroad.jt.type_list),
    bound: Option(str, 'Bound for?', choices=railroad.jt.bound_list)
):
    # crrsta, line, boundに整合性があるか
    if not railroad.jt.has_alignment(crrsta, typ):
        await ctx.respond(f'Error! There is not {crrsta} in this line!')
        return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = railroad.jt.next_station(crrsta, typ, bound, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # コメント
    cmnt = ""
    if nxtsta == crrsta:
        cmnt = "Stay here... Re-choose another train and retry!"
    if cmnt != "":
        cmnt = "\nComment> " + cmnt

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Type: {typ}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**'+cmnt)


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def ju(
    ctx,
    crrsta: Option(str, 'Current Station?', choices=railroad.ju.station_list),
    typ: Option(str, 'Which type?', choices=railroad.ju.type_list),
    bound: Option(str, 'Bound for?', choices=railroad.ju.bound_list)
):
    # crrsta, line, boundに整合性があるか
    if not railroad.ju.has_alignment(crrsta, typ):
        await ctx.respond(f'Error! There is not {crrsta} in this line!')
        return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = railroad.ju.next_station(crrsta, typ, bound, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # コメント
    cmnt = ""
    if nxtsta == crrsta:
        cmnt = "Stay here... Re-choose another train and retry!"
    if cmnt != "":
        cmnt = "\nComment> " + cmnt

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Type: {typ}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**'+cmnt)


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def jy(
    ctx,
    crrsta: Option(str, 'Current Station?'),
    loop: Option(str, 'Which loop?', choices=railroad.jy.loop_list)
):
    # crrsta, line, boundに整合性があるか
    if not railroad.jy.has_alignment(crrsta):
        await ctx.respond(f'Error! There is not {crrsta} in this line!')
        return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = railroad.jy.next_station(crrsta, loop, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # コメント
    cmnt = ""
    if nxtsta == crrsta:
        cmnt = "Stay here... Re-choose another train and retry!"
    if cmnt != "":
        cmnt = "\nComment> " + cmnt

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Loop: {loop}, Step: **{i}** ---> Next Stop: **{nxtsta}**'+cmnt)


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def twr(
    ctx,
    crrsta: Option(str, 'Current Station?', choices=railroad.twr.station_list),
    typ: Option(str, 'Which type?', choices=railroad.twr.type_list),
    bound: Option(str, 'Bound for?', choices=railroad.twr.bound_list)
):
    # crrsta, line, boundに整合性があるか
    if not railroad.twr.has_alignment(crrsta, typ):
        await ctx.respond(f'Error! There is not {crrsta} in this line!')
        return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = railroad.twr.next_station(crrsta, typ, bound, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return
    
    # WALK
    global WALK
    if WALK:
        if i == 5:
            nxtsta = railroad.twr.next_station(crrsta, "りんかい線", bound, 1)
            if nxtsta == -1:
                await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
                return
            nxtsta = "WALK TO " + nxtsta + "!"

    # コメント
    cmnt = ""
    if nxtsta == crrsta:
        cmnt = "Stay here... Re-choose another train and retry!"
    if cmnt != "":
        cmnt = "\nComment> " + cmnt

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Type: {typ}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**'+cmnt)


# Bot Run
bot.run(config.TOKEN)

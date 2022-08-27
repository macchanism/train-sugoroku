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

"""
@bot.slash_command(guild_ids=config.SERVER_IDs)
async def cmd(
    ctx,
    crrsta: Option(str, 'Current Station?'),
    line: Option(str, 'Line?', choices=railroad.env.railroad_list),
    bound: Option(str, 'Bound for?', choices=railroad.env.bound_list),
):
    # crrsta, line, boundに整合性があるか
    if not railroad.railroad_tool.is_station_in_line(crrsta, line):
        await ctx.respond(f'Error! There is not {crrsta} in this line! in {line}.')
        return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    s = railroad.railroad_tool.next_stop(crrsta, line, bound, i)
    if s == -1:
        await ctx.respond(f'Error! {line} can not be used.')
        return
    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Line: {line}, Bound: {bound}, Step: **{i}** ---> Next Stop: **{s}**')
"""


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def ja(
    ctx,
    crrsta: Option(str, 'Current Station?'),
    typ: Option(str, 'Which type?', choices=railroad.ja.type_list),
    bound: Option(str, 'Bound for?', choices=railroad.ja.bound_list)
):
    # crrsta, line, boundに整合性があるか
    if typ == "埼京線(大崎-浮間舟渡)(各駅停車)":
        if not (crrsta in railroad.ja.JA):
            await ctx.respond(f'Error! There is not {crrsta} in this line!')
            return
    elif typ == "埼京線(大崎-浮間舟渡)(快速・通勤快速)":
        if not (crrsta in railroad.ja.JA_rapid):
            await ctx.respond(f'Error! There is not {crrsta} in this line!')
            return
    elif typ == "埼京線(りんかい線直通)(各駅停車)":
        if not (crrsta in railroad.ja.JA_TWR):
            await ctx.respond(f'Error! There is not {crrsta} in this line!')
            return
    elif typ == "埼京線(りんかい線直通)(快速・通勤快速)":
        if not (crrsta in railroad.ja.JA_TWR_rapid):
            await ctx.respond(f'Error! There is not {crrsta} in this line!')
            return
    elif typ == "埼京線(相鉄線直通)(各駅停車)":
        if not (crrsta in railroad.ja.JA_SO):
            await ctx.respond(f'Error! There is not {crrsta} in this line!')
            return
    elif typ == "埼京線(相鉄線直通)(快速・通勤快速)":
        if not (crrsta in railroad.ja.JA_SO_rapid):
            await ctx.respond(f'Error! There is not {crrsta} in this line!')
            return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = -1
    if typ == "埼京線(大崎-浮間舟渡)(各駅停車)":
        nxtsta = railroad.ja.JA_res(crrsta, bound, i)
    elif typ == "埼京線(大崎-浮間舟渡)(快速・通勤快速)":
        nxtsta = railroad.ja.JA_rapid_res(crrsta, bound, i)
    elif typ == "埼京線(りんかい線直通)(各駅停車)":
        nxtsta = railroad.ja.JA_TWR_res(crrsta, bound, i)
    elif typ == "埼京線(りんかい線直通)(快速・通勤快速)":
        nxtsta = railroad.ja.JA_TWR_rapid_res(crrsta, bound, i)
    elif typ == "埼京線(相鉄線直通)(各駅停車)":
        nxtsta = railroad.ja.JA_SO_res(crrsta, bound, i)
    elif typ == "埼京線(相鉄線直通)(快速・通勤快速)":
        nxtsta = railroad.ja.JA_SO_rapid_res(crrsta, bound, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Type: {typ}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**')


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def jb(
    ctx,
    crrsta: Option(str, 'Current Station?'),
    bound: Option(str, 'Bound for?', choices=railroad.jb.bound_list)
):
    # crrsta, line, boundに整合性があるか
    if not (crrsta in railroad.jb.JB):
        await ctx.respond(f'Error! There is not {crrsta} in this line!.')
        return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = -1
    nxtsta = railroad.jb.JB_res(crrsta, bound, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**')


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def jc(
    ctx,
    crrsta: Option(str, 'Current Station?'),
    typ: Option(str, 'Which type?', choices=railroad.jc.type_list),
    bound: Option(str, 'Bound for?', choices=railroad.jc.bound_list)
):
    # crrsta, line, boundに整合性があるか
    if typ == "快速":
        if not (crrsta in railroad.jc.JC_rapid):
            await ctx.respond(f'Error! There is not {crrsta} in this line!')
            return
    elif typ == "通勤快速":
        if not (crrsta in railroad.jc.JC_commuterrapid):
            await ctx.respond(f'Error! There is not {crrsta} in this line!')
            return
    elif typ == "特別快速":
        if not (crrsta in railroad.jc.JC_specialrapid):
            await ctx.respond(f'Error! There is not {crrsta} in this line!')
            return
    elif typ == "通勤特快":
        if not (crrsta in railroad.jc.JC_commuterspecialrapid):
            await ctx.respond(f'Error! There is not {crrsta} in this line!')
            return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = -1
    if typ == "快速":
        nxtsta = railroad.jc.JC_rapid_res(crrsta, bound, i)
    elif typ == "通勤快速":
        nxtsta = railroad.jc.JC_commuterrapid_res(crrsta, bound, i)
    elif typ == "特別快速":
        nxtsta = railroad.jc.JC_specialrapid_res(crrsta, bound, i)
    elif typ == "通勤特快":
        nxtsta = railroad.jc.JC_commuterspecialrapid_res(crrsta, bound, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Type: {typ}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**')


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def je(
    ctx,
    crrsta: Option(str, 'Current Station?'),
    typ: Option(str, 'Which type?', choices=railroad.je.type_list),
    bound: Option(str, 'Bound for?', choices=railroad.je.bound_list)
):
    # crrsta, line, boundに整合性があるか
    if typ == "各駅停車":
        if not (crrsta in railroad.je.JE):
            await ctx.respond(f'Error! There is not {crrsta} in this line!.')
            return
    elif typ == "快速":
        if not (crrsta in railroad.je.JE_rapid):
            await ctx.respond(f'Error! There is not {crrsta} in this line!.')
            return
    elif typ == "通勤快速":
        if not (crrsta in railroad.je.JE_commuterrapid):
            await ctx.respond(f'Error! There is not {crrsta} in this line!.')
            return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = -1
    if typ == "各駅停車":
        nxtsta = railroad.je.JE_res(crrsta, bound, i)
    elif typ == "快速":
        nxtsta = railroad.je.JE_rapid_res(crrsta, bound, i)
    elif typ == "通勤快速":
        nxtsta = railroad.je.JE_commuterrapid_res(crrsta, bound, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Type: {typ}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**')


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def jk(
    ctx,
    crrsta: Option(str, 'Current Station?'),
    typ: Option(str, 'Which type?', choices=railroad.jk.type_list),
    bound: Option(str, 'Bound for?', choices=railroad.jk.bound_list)
):
    # crrsta, line, boundに整合性があるか
    if typ == "各駅停車":
        if not (crrsta in railroad.jk.JK):
            await ctx.respond(f'Error! There is not {crrsta} in this line!.')
            return
    elif typ == "快速":
        if not (crrsta in railroad.jk.JK_rapid):
            await ctx.respond(f'Error! There is not {crrsta} in this line!.')
            return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = -1
    if typ == "各駅停車":
        nxtsta = railroad.jk.JK_res(crrsta, bound, i)
    elif typ == "快速":
        nxtsta = railroad.jk.JK_rapid_res(crrsta, bound, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Type: {typ}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**')


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def jj(
    ctx,
    crrsta: Option(str, 'Current Station?'),
    typ: Option(str, 'Which type?', choices=railroad.jj.type_list),
    bound: Option(str, 'Bound for?', choices=railroad.jj.bound_list)
):
    # crrsta, line, boundに整合性があるか
    if typ == "常磐線快速(上野-北千住)(普通・快速)":
        if not (crrsta in railroad.jj.JJ):
            await ctx.respond(f'Error! There is not {crrsta} in this line!')
            return
    elif typ == "常磐線快速(上野-北千住)(特別快速)":
        if not (crrsta in railroad.jj.JJ_specialrapid):
            await ctx.respond(f'Error! There is not {crrsta} in this line!')
            return
    elif typ == "上野東京ライン(常磐線快速・東海道線直通)(普通・快速)":
        if not (crrsta in railroad.jj.UTL_JJ):
            await ctx.respond(f'Error! There is not {crrsta} in this line!')
            return
    elif typ == "上野東京ライン(常磐線快速・東海道線直通)(特別快速)":
        if not (crrsta in railroad.jj.UTL_JJ_specialrapid):
            await ctx.respond(f'Error! There is not {crrsta} in this line!')
            return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = -1
    if typ == "常磐線快速(上野-北千住)(普通・快速)":
        nxtsta = railroad.jj.JJ_res(crrsta, bound, i)
    elif typ == "常磐線快速(上野-北千住)(特別快速)":
        nxtsta = railroad.jj.JJ_specialrapid_res(crrsta, bound, i)
    elif typ == "上野東京ライン(常磐線快速・東海道線直通)(普通・快速)":
        nxtsta = railroad.jj.UTL_JJ_res(crrsta, bound, i)
    elif typ == "上野東京ライン(常磐線快速・東海道線直通)(特別快速)":
        nxtsta = railroad.jj.UTL_JJ_specialrapid_res(crrsta, bound, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Type: {typ}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**')


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def jl(
    ctx,
    crrsta: Option(str, 'Current Station?'),
    bound: Option(str, 'Bound for?', choices=railroad.jl.bound_list)
):
    # crrsta, line, boundに整合性があるか
    if not (crrsta in railroad.jl.JL):
        await ctx.respond(f'Error! There is not {crrsta} in this line!.')
        return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = -1
    nxtsta = railroad.jl.JL_res(crrsta, bound, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**')


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def jo(
    ctx,
    crrsta: Option(str, 'Current Station?'),
    bound: Option(str, 'Bound for?', choices=railroad.jo.bound_list)
):
    # crrsta, line, boundに整合性があるか
    if not (crrsta in railroad.jo.JO):
        await ctx.respond(f'Error! There is not {crrsta} in this line!.')
        return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = -1
    nxtsta = railroad.jo.JO_res(crrsta, bound, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**')


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def js(
    ctx,
    crrsta: Option(str, 'Current Station?'),
    typ: Option(str, 'Which type?', choices=railroad.js.type_list),
    bound: Option(str, 'Bound for?', choices=railroad.js.bound_list)
):
    # crrsta, line, boundに整合性があるか
    if typ == "宇都宮線・横須賀線直通(普通・快速)":
        if not (crrsta in railroad.js.JS_U_JO):
            await ctx.respond(f'Error! There is not {crrsta} in this line!')
            return
    elif typ == "高崎線・東海道線直通(普通・快速)":
        if not (crrsta in railroad.js.JS_T_JT):
            await ctx.respond(f'Error! There is not {crrsta} in this line!')
            return
    elif typ == "高崎線・東海道線直通(特別快速)":
        if not (crrsta in railroad.js.JS_T_JT_specialrapd):
            await ctx.respond(f'Error! There is not {crrsta} in this line!')
            return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = -1
    if typ == "宇都宮線・横須賀線直通(普通・快速)":
        nxtsta = railroad.js.JS_U_JO_res(crrsta, bound, i)
    elif typ == "高崎線・東海道線直通(普通・快速)":
        nxtsta = railroad.js.JS_T_JT_res(crrsta, bound, i)
    elif typ == "高崎線・東海道線直通(特別快速)":
        nxtsta = railroad.js.JS_T_JT_specialrapd_res(crrsta, bound, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Type: {typ}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**')


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def jy(
    ctx,
    crrsta: Option(str, 'Current Station?'),
    loop: Option(str, 'Which loop?', choices=railroad.jy.loop_list)
):
    # crrsta, line, boundに整合性があるか
    if not (crrsta in railroad.jy.JY):
        await ctx.respond(f'Error! There is not {crrsta} in this line!')
        return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = -1
    if loop == "内回り":
        nxtsta = railroad.jy.JY_inner_res(crrsta, i)
    elif loop == "外回り":
        nxtsta = railroad.jy.JY_outer_res(crrsta, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Loop: {loop}, Step: **{i}** ---> Next Stop: **{nxtsta}**')


@bot.slash_command(guild_ids=config.SERVER_IDs)
async def twr(
    ctx,
    crrsta: Option(str, 'Current Station?'),
    typ: Option(str, 'Which type?', choices=railroad.twr.type_list),
    bound: Option(str, 'Bound for?', choices=railroad.twr.bound_list)
):
    # crrsta, line, boundに整合性があるか
    if typ == "りんかい線":
        if not (crrsta in railroad.twr.TWR):
            await ctx.respond(f'Error! There is not {crrsta} in this line!')
            return
    elif typ == "りんかい線(埼京線直通)(各駅停車)":
        if not (crrsta in railroad.twr.TWR_JA):
            await ctx.respond(f'Error! There is not {crrsta} in this line!')
            return
    elif typ == "りんかい線(埼京線直通)(快速・通勤快速)":
        if not (crrsta in railroad.twr.TWR_JA_rapid):
            await ctx.respond(f'Error! There is not {crrsta} in this line!')
            return

    # サイコロを振る
    i = tool.Dice(5)

    # 出目から結果をサーチ
    nxtsta = -1
    if typ == "りんかい線":
        nxtsta = railroad.twr.TWR_res(crrsta, bound, i)
    elif typ == "りんかい線(埼京線直通)(各駅停車)":
        nxtsta = railroad.twr.TWR_JA_res(crrsta, bound, i)
    elif typ == "りんかい線(埼京線直通)(快速・通勤快速)":
        nxtsta = railroad.twr.TWR_JA_rapid_res(crrsta, bound, i)
    if nxtsta == -1:
        await ctx.respond(f'Error! コマンドの引数を見直すか, GMに連絡してください')
        return

    # 出力
    await ctx.respond(f'Current Station: {crrsta}, Type: {typ}, Bound for: {bound}, Step: **{i}** ---> Next Stop: **{nxtsta}**')


bot.run(config.TOKEN)

# 常磐線快速(普通・快速)(上野-北千住), 常磐線快速(特別快速)(上野-北千住)
# 上野東京ライン(常磐線快速・東海道線直通)(普通・快速), 上野東京ライン(常磐線快速・東海道線直通)(特別快速)
JJ = ["上野", "日暮里", "三河島", "南千住", "北千住"]
JJ_specialrapid = ["上野", "日暮里", "北千住"]
UTL_JJ = ["品川", "新橋", "東京"] + JJ
UTL_JJ_specialrapid =  ["品川", "新橋", "東京"] + JJ_specialrapid

station_list = ["北千住", "南千住", "三河島", "日暮里", "上野", "東京", "新橋", "品川"]

type_list = ["常磐線快速(上野-北千住)(普通・快速)", "常磐線快速(上野-北千住)(特別快速)", "上野東京ライン(常磐線快速・東海道線直通)(普通・快速)", "上野東京ライン(常磐線快速・東海道線直通)(特別快速)"]

bound_list = ["品川", "上野", "北千住 以東"]


def endstation(b):
    if b == "北千住 以東":
        return "北千住"
    return b

def JJ_res(crr, b, i):
    e = endstation(b)
    idx_crr = JJ.index(crr)
    idx_end = JJ.index(e)
    if idx_crr < idx_end:
        return JJ[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JJ[max(idx_crr - i, idx_end)]
    return crr

def JJ_specialrapid_res(crr, b, i):
    e = endstation(b)
    idx_crr = JJ_specialrapid.index(crr)
    idx_end = JJ_specialrapid.index(e)
    if idx_crr < idx_end:
        return JJ_specialrapid[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JJ_specialrapid[max(idx_crr - i, idx_end)]
    return crr

def UTL_JJ_res(crr, b, i):
    e = endstation(b)
    idx_crr = UTL_JJ.index(crr)
    idx_end = UTL_JJ.index(e)
    if idx_crr < idx_end:
        return UTL_JJ[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return UTL_JJ[max(idx_crr - i, idx_end)]
    return crr

def UTL_JJ_specialrapid_res(crr, b, i):
    e = endstation(b)
    idx_crr = UTL_JJ_specialrapid.index(crr)
    idx_end = UTL_JJ_specialrapid.index(e)
    if idx_crr < idx_end:
        return UTL_JJ_specialrapid[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return UTL_JJ_specialrapid[max(idx_crr - i, idx_end)]
    return crr

# 東海道線(東京-品川)
# 上野東京ライン(宇都宮線・高崎線・東海道線直通)(普通), 上野東京ライン(宇都宮線・高崎線・東海道線直通)(快速)
# 上野東京ライン(常磐線快速・東海道線直通)(普通・快速), 上野東京ライン(常磐線快速・東海道線直通)(特別快速)
JT = ["東京", "新橋", "品川"]

UTL_JT_JU = ["赤羽", "尾久", "上野"] + JT
UTL_JT_JU_rapid = ["赤羽", "上野"] + JT

UTL_JT_JJ = ["北千住", "南千住", "三河島", "日暮里", "上野"] + JT
UTL_JT_JJ_specialrapid = ["北千住", "日暮里", "上野"] + JT

station_list = ["品川", "新橋", "東京", "上野", "尾久", "赤羽", "日暮里", "三河島", "南千住", "北千住"]

type_list = ["東海道線(東京-品川)", "上野東京ライン(宇都宮線・高崎線・東海道線直通)(普通)", "上野東京ライン(宇都宮線・高崎線・東海道線直通)(快速)", "上野東京ライン(常磐線快速・東海道線直通)(普通・快速)", "上野東京ライン(常磐線快速・東海道線直通)(特別快速)"]

bound_list = ["品川 以南", "東京", "上野", "赤羽 以北", "北千住 以東"]


def endstation(b):
    if b == "品川 以南":
        return "品川"
    elif b == "赤羽 以北":
        return "赤羽"
    elif b == "北千住 以東":
        return "北千住"
    return b

def JT_res(crr, b, i):
    e = endstation(b)
    idx_crr = JT.index(crr)
    idx_end = JT.index(e)
    if idx_crr < idx_end:
        return JT[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JT[max(idx_crr - i, idx_end)]
    return crr

def UTL_JT_JU_res(crr, b, i):
    e = endstation(b)
    idx_crr = UTL_JT_JU.index(crr)
    idx_end = UTL_JT_JU.index(e)
    if idx_crr < idx_end:
        return UTL_JT_JU[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return UTL_JT_JU[max(idx_crr - i, idx_end)]
    return crr

def UTL_JT_JU_rapid_res(crr, b, i):
    e = endstation(b)
    idx_crr = UTL_JT_JU_rapid.index(crr)
    idx_end = UTL_JT_JU_rapid.index(e)
    if idx_crr < idx_end:
        return UTL_JT_JU_rapid[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return UTL_JT_JU_rapid[max(idx_crr - i, idx_end)]
    return crr

def UTL_JT_JJ_res(crr, b, i):
    e = endstation(b)
    idx_crr = UTL_JT_JJ.index(crr)
    idx_end = UTL_JT_JJ.index(e)
    if idx_crr < idx_end:
        return UTL_JT_JJ[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return UTL_JT_JJ[max(idx_crr - i, idx_end)]
    return crr

def UTL_JT_JJ_specialrapid_res(crr, b, i):
    e = endstation(b)
    idx_crr = UTL_JT_JJ_specialrapid.index(crr)
    idx_end = UTL_JT_JJ_specialrapid.index(e)
    if idx_crr < idx_end:
        return UTL_JT_JJ_specialrapid[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return UTL_JT_JJ_specialrapid[max(idx_crr - i, idx_end)]
    return crr

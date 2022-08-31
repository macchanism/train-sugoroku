# 宇都宮線・高崎線(上野-赤羽)(普通), 宇都宮線・高崎線(上野-赤羽)(快速)
# 上野東京ライン(宇都宮線・高崎線・東海道線直通)(普通), 上野東京ライン(宇都宮線・高崎線・東海道線直通)(快速)
JU = ["上野", "尾久", "赤羽"]
JU_rapid = ["上野", "赤羽"]
UTL_JU = ["品川", "新橋", "東京"] + JU
UTL_JU_rapid =  ["品川", "新橋", "東京"] + JU_rapid

station_list = ["赤羽", "尾久", "上野", "東京", "新橋", "品川"]

type_list = ["宇都宮線・高崎線(上野-赤羽)(普通)", "宇都宮線・高崎線(上野-赤羽)(快速)", "上野東京ライン(宇都宮線・高崎線・東海道線直通)(普通)", "上野東京ライン(宇都宮線・高崎線・東海道線直通)(快速)"]

bound_list = ["品川 以南", "東京", "上野", "赤羽 以北"]


def endstation(b):
    if b == "赤羽 以北":
        return "赤羽"
    elif b == "品川 以南":
        return "品川"
    return b

def JU_res(crr, b, i):
    e = endstation(b)
    idx_crr = JU.index(crr)
    idx_end = JU.index(e)
    if idx_crr < idx_end:
        return JU[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JU[max(idx_crr - i, idx_end)]
    return crr

def JU_rapid_res(crr, b, i):
    e = endstation(b)
    idx_crr = JU_rapid.index(crr)
    idx_end = JU_rapid.index(e)
    if idx_crr < idx_end:
        return JU_rapid[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JU_rapid[max(idx_crr - i, idx_end)]
    return crr

def UTL_JU_res(crr, b, i):
    e = endstation(b)
    idx_crr = UTL_JU.index(crr)
    idx_end = UTL_JU.index(e)
    if idx_crr < idx_end:
        return UTL_JU[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return UTL_JU[max(idx_crr - i, idx_end)]
    return crr

def UTL_JU_rapid_res(crr, b, i):
    e = endstation(b)
    idx_crr = UTL_JU_rapid.index(crr)
    idx_end = UTL_JU_rapid.index(e)
    if idx_crr < idx_end:
        return UTL_JU_rapid[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return UTL_JU_rapid[max(idx_crr - i, idx_end)]
    return crr


def has_alignment(current_station, train_type):
    if train_type == "宇都宮線・高崎線(上野-赤羽)(普通)":
        return (current_station in JU)
    elif train_type == "宇都宮線・高崎線(上野-赤羽)(快速)":
        return (current_station in JU_rapid)
    elif train_type == "上野東京ライン(宇都宮線・高崎線・東海道線直通)(普通)":
        return (current_station in UTL_JU)
    elif train_type == "上野東京ライン(宇都宮線・高崎線・東海道線直通)(快速)":
        return (current_station in UTL_JU_rapid)
    return False

def next_station(current_station, train_type, train_bound, step):
    ret = -1
    if train_type == "宇都宮線・高崎線(上野-赤羽)(普通)":
        ret = JU_res(current_station, train_bound, step)
    elif train_type == "宇都宮線・高崎線(上野-赤羽)(快速)":
        ret = JU_rapid_res(current_station, train_bound, step)
    elif train_type == "上野東京ライン(宇都宮線・高崎線・東海道線直通)(普通)":
        ret = UTL_JU_res(current_station, train_bound, step)
    elif train_type == "上野東京ライン(宇都宮線・高崎線・東海道線直通)(快速)":
        ret = UTL_JU_rapid_res(current_station, train_bound, step)
    return ret

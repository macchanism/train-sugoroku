# 湘南新宿ライン
JS_U_JO = ["西大井", "大崎", "恵比寿", "渋谷", "新宿", "池袋", "赤羽"]
JS_T_JT = ["大崎", "恵比寿", "渋谷", "新宿", "池袋", "赤羽"]
JS_T_JT_specialrapd = ["大崎", "渋谷", "新宿", "池袋", "赤羽"]

station_list = ["赤羽", "池袋", "新宿", "渋谷", "恵比寿", "大崎", "西大井"]

type_list = ["宇都宮線・横須賀線直通(普通・快速)", "高崎線・東海道線直通(普通・快速)", "高崎線・東海道線直通(特別快速)"]

bound_list = ["西大井 以南", "赤羽 以北"]


def endstation(b, p):
    if b == "赤羽 以北":
        return "赤羽"
    elif b == "西大井 以南":
        if p == 1:
            return "大崎"
        return "西大井"
    return b

def JS_U_JO_res(crr, b, i):
    e = endstation(b, 0)
    idx_crr = JS_U_JO.index(crr)
    idx_end = JS_U_JO.index(e)
    if idx_crr < idx_end:
        return JS_U_JO[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JS_U_JO[max(idx_crr - i, idx_end)]
    return crr

def JS_T_JT_res(crr, b, i):
    e = endstation(b, 1)
    idx_crr = JS_T_JT.index(crr)
    idx_end = JS_T_JT.index(e)
    if idx_crr < idx_end:
        return JS_T_JT[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JS_T_JT[max(idx_crr - i, idx_end)]
    return crr

def JS_T_JT_specialrapd_res(crr, b, i):
    e = endstation(b, 1)
    idx_crr = JS_T_JT_specialrapd.index(crr)
    idx_end = JS_T_JT_specialrapd.index(e)
    if idx_crr < idx_end:
        return JS_T_JT_specialrapd[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JS_T_JT_specialrapd[max(idx_crr - i, idx_end)]
    return crr


def has_alignment(current_station, train_type):
    if train_type == "宇都宮線・横須賀線直通(普通・快速)":
        return (current_station in JS_U_JO)
    elif train_type == "高崎線・東海道線直通(普通・快速)":
        return (current_station in JS_T_JT)
    elif train_type == "高崎線・東海道線直通(特別快速)":
        return (current_station in JS_T_JT_specialrapd)
    return False

def next_station(current_station, train_type, train_bound, step):
    ret = -1
    if train_type == "宇都宮線・横須賀線直通(普通・快速)":
        ret = JS_U_JO_res(current_station, train_bound, step)
    elif train_type == "高崎線・東海道線直通(普通・快速)":
        ret = JS_T_JT_res(current_station, train_bound, step)
    elif train_type == "高崎線・東海道線直通(特別快速)":
        ret = JS_T_JT_specialrapd_res(current_station, train_bound, step)
    return ret

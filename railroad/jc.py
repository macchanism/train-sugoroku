# 中央線快速
JC_rapid = ["東京", "神田", "御茶ノ水", "四ツ谷", "新宿", "中野", "高円寺", "阿佐ヶ谷", "荻窪", "西荻窪"]
JC_commuterrapid = ["東京", "神田", "御茶ノ水", "四ツ谷", "新宿", "中野", "荻窪"]
JC_specialrapid = ["東京", "神田", "御茶ノ水", "四ツ谷", "新宿", "中野"]
JC_commuterspecialrapid = ["東京", "神田", "御茶ノ水", "四ツ谷", "新宿"]
JC_rapid_holiday = ["東京", "神田", "御茶ノ水", "四ツ谷", "新宿", "中野", "荻窪"]

station_list = ["東京", "神田", "御茶ノ水", "四ツ谷", "新宿", "中野", "高円寺", "阿佐ヶ谷", "荻窪", "西荻窪"]

type_list = ["快速", "通勤快速", "特別快速", "通勤特快"]

bound_list = ["東京", "下り方面"]


def JC_rapid_res(crr, b, i):
    idx_crr = JC_rapid.index(crr)
    if b == "下り方面":
        return JC_rapid[min(idx_crr + i, len(JC_rapid)-1)]
    elif b == "東京":
        return JC_rapid[max(idx_crr - i, 0)]
    return crr

def JC_commuterrapid_res(crr, b, i):
    idx_crr = JC_commuterrapid.index(crr)
    if b == "下り方面":
        return JC_commuterrapid[min(idx_crr + i, len(JC_commuterrapid)-1)]
    elif b == "東京":
        return JC_commuterrapid[max(idx_crr - i, 0)]
    return crr

def JC_specialrapid_res(crr, b, i):
    idx_crr = JC_specialrapid.index(crr)
    if b == "下り方面":
        return JC_specialrapid[min(idx_crr + i, len(JC_specialrapid)-1)]
    elif b == "東京":
        return JC_specialrapid[max(idx_crr - i, 0)]
    return crr

def JC_commuterspecialrapid_res(crr, b, i):
    idx_crr = JC_commuterspecialrapid.index(crr)
    if b == "下り方面":
        return JC_commuterspecialrapid[min(idx_crr + i, len(JC_commuterspecialrapid)-1)]
    elif b == "東京":
        return JC_commuterspecialrapid[max(idx_crr - i, 0)]
    return crr

def JC_rapid_holiday_res(crr, b, i):
    idx_crr = JC_rapid_holiday.index(crr)
    if b == "下り方面":
        return JC_rapid_holiday[min(idx_crr + i, len(JC_rapid_holiday)-1)]
    elif b == "東京":
        return JC_rapid_holiday[max(idx_crr - i, 0)]
    return crr


def has_alignment(current_station, train_type, holiday):
    if train_type == "快速":
        if not holiday:
            return (current_station in JC_rapid)
        else:
            return (current_station in JC_rapid_holiday)
    elif train_type == "通勤快速":
        return (current_station in JC_commuterrapid)
    elif train_type == "特別快速":
        return (current_station in JC_specialrapid)
    elif train_type == "通勤特快":
        return (current_station in JC_commuterspecialrapid)
    return False

def next_station(current_station, train_type, train_bound, step, holiday):
    ret = -1
    if train_type == "快速":
        if not holiday:
           ret = JC_rapid_res(current_station, train_bound, step)
        else:
            ret = JC_rapid_holiday_res(current_station, train_bound, step)
    elif train_type == "通勤快速":
        ret = JC_commuterrapid_res(current_station, train_bound, step)
    elif train_type == "特別快速":
        ret = JC_specialrapid_res(current_station, train_bound, step)
    elif train_type == "通勤特快":
        ret = JC_commuterspecialrapid_res(current_station, train_bound, step)
    return ret

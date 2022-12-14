# 京葉線
JE = ["東京", "八丁堀", "越中島", "潮見", "新木場", "葛西臨海公園"]
JE_rapid = ["東京", "八丁堀", "新木場"]

station_list = ["東京", "八丁堀", "越中島", "潮見", "新木場", "葛西臨海公園"]

type_list = ["各駅停車", "快速・通勤快速"]

bound_list = ["東京", "下り方面"]


def JE_res(crr, b, i):
    idx_crr = JE.index(crr)

    if b == "下り方面":
        return JE[min(idx_crr + i, len(JE)-1)]
    elif b == "東京":
        return JE[max(idx_crr - i, 0)]

    return crr

def JE_rapid_res(crr, b, i):
    idx_crr = JE_rapid.index(crr)

    if b == "下り方面":
        return JE_rapid[min(idx_crr + i, len(JE_rapid)-1)]
    elif b == "東京":
        return JE_rapid[max(idx_crr - i, 0)]

    return crr


def has_alignment(current_station, train_type):
    if train_type == "各駅停車":
        return (current_station in JE)
    elif train_type == "快速・通勤快速":
        return (current_station in JE_rapid)
    return False

def next_station(current_station, train_type, train_bound, step):
    ret = -1
    if train_type == "各駅停車":
        ret = JE_res(current_station, train_bound, step)
    elif train_type == "快速・通勤快速":
        ret = JE_rapid_res(current_station, train_bound, step)
    return ret

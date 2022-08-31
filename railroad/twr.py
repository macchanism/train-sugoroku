# りんかい線, りんかい線(埼京線直通)(各駅停車), りんかい線(埼京線直通)(快速・通勤快速)
TWR = ["新木場", "東雲", "国際展示場", "東京テレポート", "天王洲アイル", "品川シーサイド", "大井町", "大崎"]

JA = ["大崎", "恵比寿", "渋谷", "新宿", "池袋", "板橋", "十条", "赤羽", "北赤羽", "浮間舟渡"]
JA_rapid = ["大崎", "恵比寿", "渋谷", "新宿", "池袋", "板橋", "十条", "赤羽"]

TWR_JA = TWR + JA[1:]
TWR_JA_rapid = TWR + JA_rapid[1:]

station_list = ["大崎", "大井町", "品川シーサイド", "天王洲アイル", "東京テレポート", "国際展示場", "東雲", "新木場"]

type_list = ["りんかい線", "りんかい線(埼京線直通)(各駅停車)", "りんかい線(埼京線直通)(快速・通勤快速)"]

bound_list = ["新木場", "東京テレポート", "大崎", "新宿", "池袋", "赤羽", "浮間舟渡 以北"]


def endstation(b, p):
    if b == "浮間舟渡 以北":
        if p == 1:
            return "赤羽"
        return "浮間舟渡"
    return b

def TWR_res(crr, b, i):
    e = endstation(b, 0)
    idx_crr = TWR.index(crr)
    idx_end = TWR.index(e)
    if idx_crr < idx_end:
        return TWR[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return TWR[max(idx_crr - i, idx_end)]
    return crr

def TWR_JA_res(crr, b, i):
    e = endstation(b, 0)
    idx_crr = TWR_JA.index(crr)
    idx_end = TWR_JA.index(e)
    if idx_crr < idx_end:
        return TWR_JA[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return TWR_JA[max(idx_crr - i, idx_end)]
    return crr

def TWR_JA_rapid_res(crr, b, i):
    e = endstation(b, 1)
    idx_crr = TWR_JA_rapid.index(crr)
    idx_end = TWR_JA_rapid.index(e)
    if idx_crr < idx_end:
        return TWR_JA_rapid[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return TWR_JA_rapid[max(idx_crr - i, idx_end)]
    return crr


def has_alignment(current_station, train_type):
    if train_type == "りんかい線":
        return (current_station in TWR)
    elif train_type == "りんかい線(埼京線直通)(各駅停車)":
        return (current_station in TWR_JA)
    elif train_type == "りんかい線(埼京線直通)(快速・通勤快速)":
        return (current_station in TWR_JA_rapid)
    return False

def next_station(current_station, train_type, train_bound, step):
    ret = -1
    if train_type == "りんかい線":
        ret = TWR_res(current_station, train_bound, step)
    elif train_type == "りんかい線(埼京線直通)(各駅停車)":
        ret = TWR_JA_res(current_station, train_bound, step)
    elif train_type == "りんかい線(埼京線直通)(快速・通勤快速)":
        ret = TWR_JA_rapid_res(current_station, train_bound, step)
    return ret

# 埼京線(大崎-浮間舟渡), 埼京線(りんかい線直通), 埼京線(相鉄線直通)
JA = ["大崎", "恵比寿", "渋谷", "新宿", "池袋", "板橋", "十条", "赤羽", "北赤羽", "浮間舟渡"]
JA_rapid = ["大崎", "恵比寿", "渋谷", "新宿", "池袋", "板橋", "十条", "赤羽"]

TWR = ["新木場", "東雲", "国際展示場", "東京テレポート", "天王洲アイル", "品川シーサイド", "大井町", "大崎"]

JA_TWR = TWR + JA[1:]
JA_TWR_rapid = TWR + JA_rapid[1:]

JA_SO = ["西大井"] + JA
JA_SO_rapid = ["西大井"] + JA_rapid

station_list = ["浮間舟渡", "北赤羽", "赤羽", "十条", "板橋", "池袋", "新宿", "渋谷", "恵比寿", "大崎", "西大井"]

type_list = ["埼京線(大崎-浮間舟渡)(各駅停車)", "埼京線(大崎-浮間舟渡)(快速・通勤快速)", "埼京線(りんかい線直通)(各駅停車)", "埼京線(りんかい線直通)(快速・通勤快速)", "埼京線(相鉄線直通)(各駅停車)", "埼京線(相鉄線直通)(快速・通勤快速)"]

bound_list = ["西大井 以南", "新木場", "東京テレポート", "大崎", "新宿", "池袋", "赤羽", "浮間舟渡 以北"]


def endstation(b, p):
    if b == "西大井 以南":
        return "西大井"
    elif b == "浮間舟渡 以北":
        if p == 1:
            return "赤羽"
        return "浮間舟渡"
    return b

def JA_res(crr, b, i):
    e = endstation(b, 0)
    idx_crr = JA.index(crr)
    idx_end = JA.index(e)
    if idx_crr < idx_end:
        return JA[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JA[max(idx_crr - i, idx_end)]
    return crr

def JA_TWR_res(crr, b, i):
    e = endstation(b, 0)
    idx_crr = JA_TWR.index(crr)
    idx_end = JA_TWR.index(e)
    if idx_crr < idx_end:
        return JA_TWR[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JA_TWR[max(idx_crr - i, idx_end)]
    return crr

def JA_SO_res(crr, b, i):
    e = endstation(b, 0)
    idx_crr = JA_SO.index(crr)
    idx_end = JA_SO.index(e)
    if idx_crr < idx_end:
        return JA_SO[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JA_SO[max(idx_crr - i, idx_end)]
    return crr

def JA_rapid_res(crr, b, i):
    e = endstation(b, 1)
    idx_crr = JA_rapid.index(crr)
    idx_end = JA_rapid.index(e)
    if idx_crr < idx_end:
        return JA_rapid[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JA_rapid[max(idx_crr - i, idx_end)]
    return crr

def JA_TWR_rapid_res(crr, b, i):
    e = endstation(b, 1)
    idx_crr = JA_TWR_rapid.index(crr)
    idx_end = JA_TWR_rapid.index(e)
    if idx_crr < idx_end:
        return JA_TWR_rapid[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JA_TWR_rapid[max(idx_crr - i, idx_end)]
    return crr

def JA_SO_rapid_res(crr, b, i):
    e = endstation(b, 1)
    idx_crr = JA_SO_rapid.index(crr)
    idx_end = JA_SO_rapid.index(e)
    if idx_crr < idx_end:
        return JA_SO_rapid[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JA_SO_rapid[max(idx_crr - i, idx_end)]
    return crr

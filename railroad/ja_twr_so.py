# 埼京線(浮間舟渡-大崎), 埼京線(りんかい線直通), 埼京線(相鉄線直通), りんかい線
JA = ["大崎", "恵比寿", "渋谷", "新宿", "池袋", "板橋", "十条", "赤羽", "北赤羽", "浮間舟渡"]
TWR = ["新木場", "東雲", "国際展示場", "東京テレポート", "天王洲アイル", "品川シーサイド", "大井町", "大崎"]
JA_TWR = TWR + JA[1:]
JA_SO = ["西大井"] + JA


def endstation(b):
    if b == "浮間舟渡 以北":
        return "浮間舟渡"
    elif b == "西大井 以南":
        return "西大井"
    return b

def JA_res(crr, b, i):
    e = endstation(b)
    idx_crr = JA.index(crr)
    idx_end = JA.index(e)
    if idx_crr < idx_end:
        return JA[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JA[max(idx_crr - i, idx_end)]
    return crr

def JA_TWR_res(crr, b, i):
    e = endstation(b)
    idx_crr = JA_TWR.index(crr)
    idx_end = JA_TWR.index(e)
    if idx_crr < idx_end:
        return JA_TWR[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JA_TWR[max(idx_crr - i, idx_end)]
    return crr

def JA_SO_res(crr, b, i):
    e = endstation(b)
    idx_crr = JA_SO.index(crr)
    idx_end = JA_SO.index(e)
    if idx_crr < idx_end:
        return JA_SO[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JA_SO[max(idx_crr - i, idx_end)]
    return crr

def TWR_res(crr, b, i):
    e = endstation(b)
    idx_crr = TWR.index(crr)
    idx_end = TWR.index(e)
    if idx_crr < idx_end:
        return TWR[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return TWR[max(idx_crr - i, idx_end)]
    return crr
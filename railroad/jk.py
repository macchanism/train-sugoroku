# 京浜東北線
JK = ["蒲田", "大森", "大井町", "品川", "高輪ゲートウェイ", "田町", "浜松町", "新橋", "有楽町", "東京", "神田", "秋葉原", "御徒町", "上野", "鶯谷", "日暮里", "西日暮里", "田端", "上中里", "王子", "東十条", "赤羽"]
JK_rapid = ["蒲田", "大森", "大井町", "品川", "高輪ゲートウェイ", "田町", "浜松町", "東京", "神田", "秋葉原", "上野", "田端", "上中里", "王子", "東十条", "赤羽"]
JK_rapid_holiday = ["蒲田", "大森", "大井町", "品川", "高輪ゲートウェイ", "田町", "浜松町", "東京", "神田", "秋葉原", "御徒町", "上野", "田端", "上中里", "王子", "東十条", "赤羽"]


def endstation(b):
    if b in ["大宮", "南浦和"]:
        return "赤羽"
    elif b in ["鶴見", "東神奈川", "桜木町", "磯子", "大船"]:
        return "蒲田"
    return b

def JK_res(crr, b, i):
    e = endstation(b)
    idx_crr = JK.index(crr)
    idx_end = JK.index(e)
    if idx_crr < idx_end:
        return JK[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JK[max(idx_crr - i, idx_end)]
    return crr

def JK_rapid_res(crr, b, i):
    e = endstation(b)
    idx_crr = JK_rapid.index(crr)
    idx_end = JK_rapid.index(e)
    if idx_crr < idx_end:
        return JK_rapid[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JK_rapid[max(idx_crr - i, idx_end)]
    return crr

# 京浜東北線
JK = ["蒲田", "大森", "大井町", "品川", "高輪ゲートウェイ", "田町", "浜松町", "新橋", "有楽町", "東京", "神田", "秋葉原", "御徒町", "上野", "鶯谷", "日暮里", "西日暮里", "田端", "上中里", "王子", "東十条", "赤羽"]
JK_rapid = ["蒲田", "大森", "大井町", "品川", "高輪ゲートウェイ", "田町", "浜松町", "東京", "神田", "秋葉原", "上野", "田端", "上中里", "王子", "東十条", "赤羽"]
#JK_rapid_holiday = ["蒲田", "大森", "大井町", "品川", "高輪ゲートウェイ", "田町", "浜松町", "東京", "神田", "秋葉原", "御徒町", "上野", "田端", "上中里", "王子", "東十条", "赤羽"]

station_list = ["赤羽", "東十条", "王子", "上中里", "田端", "西日暮里", "日暮里", "鶯谷", "上野", "御徒町", "秋葉原", "神田", "東京", "有楽町", "新橋", "浜松町", "田町", "高輪ゲートウェイ", "品川", "大井町", "大森", "蒲田"]

type_list = ["各駅停車", "快速"]

bound_list = ["蒲田 以南", "品川", "東京", "上野", "東十条", "赤羽 以北"]


def endstation(b):
    if b == "蒲田 以南":
        return "蒲田"
    elif b == "赤羽 以北":
        return "赤羽"
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

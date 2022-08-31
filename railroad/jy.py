# 山手線
JY = ["東京", "神田", "秋葉原", "御徒町", "上野", "鶯谷", "日暮里", "西日暮里", "田端", "駒込", "巣鴨", "大塚", "池袋", "目白", "高田馬場", "新大久保", "新宿", "代々木", "原宿", "渋谷", "恵比寿", "目黒", "五反田", "大崎", "品川", "高輪ゲートウェイ", "田町", "浜松町", "新橋", "有楽町"]

loop_list = ["内回り", "外回り"]


def JY_inner_res(crr, step):
    return JY[(JY.index(crr) + step) % len(JY)]

def JY_outer_res(crr, step):
    return JY[(JY.index(crr) - step)]


def has_alignment(current_station):
    return (current_station in JY)

def next_station(current_station, loop, step):
    ret = -1
    if loop == "内回り":
        ret = JY_inner_res(current_station, step)
    elif loop == "外回り":
        ret = JY_outer_res(current_station, step)
    return ret

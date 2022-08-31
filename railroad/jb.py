# 総武線各停・中央線各停
JB = ["西荻窪", "荻窪", "阿佐ヶ谷", "高円寺", "中野", "東中野", "大久保", "新宿", "代々木", "千駄ヶ谷", "信濃町", "四ツ谷", "市ヶ谷", "飯田橋", "水道橋", "御茶ノ水", "秋葉原", "浅草橋", "両国", "錦糸町", "亀戸", "平井", "新小岩", "小岩"]

station_list = ["西荻窪", "荻窪", "阿佐ヶ谷", "高円寺", "中野", "東中野", "大久保", "新宿", "代々木", "千駄ヶ谷", "信濃町", "四ツ谷", "市ヶ谷", "飯田橋", "水道橋", "御茶ノ水", "秋葉原", "浅草橋", "両国", "錦糸町", "亀戸", "平井", "新小岩", "小岩"]

bound_list = ["西荻窪 以西", "中野", "御茶ノ水", "小岩 以東"]


def endstation(b):
    if b == "西荻窪 以西":
        return "西荻窪"
    elif b == "小岩 以東":
        return "小岩"
    return b

def JB_res(crr, b, i):
    e = endstation(b)
    idx_crr = JB.index(crr)
    idx_end = JB.index(e)
    if idx_crr < idx_end:
        return JB[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JB[max(idx_crr - i, idx_end)]
    return crr


def has_alignment(current_station):
    return (current_station in JB)

def next_station(current_station, train_bound, step):
    ret = -1
    ret = JB_res(current_station, train_bound, step)
    return ret

# 横須賀瀬・総武線快速
JO = ["西大井", "品川", "新橋", "東京", "新日本橋", "馬喰町", "錦糸町", "新小岩"]

station_list = ["西大井", "品川", "新橋", "東京", "新日本橋", "馬喰町", "錦糸町", "新小岩"]

bound_list = ["西大井 以南", "品川", "東京", "新小岩 以東"]


def endstation(b):
    if b == "西大井 以南":
        return "西大井"
    elif b == "新小岩 以東":
        return "新小岩"
    return b

def JO_res(crr, b, i):
    e = endstation(b)
    idx_crr = JO.index(crr)
    idx_end = JO.index(e)
    if idx_crr < idx_end:
        return JO[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JO[max(idx_crr - i, idx_end)]
    return crr


def has_alignment(current_station):
    return (current_station in JO)

def next_station(current_station, train_bound, step):
    ret = -1
    ret = JO_res(current_station, train_bound, step)
    return ret

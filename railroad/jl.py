# 常磐線各駅停車(北千住-金町)
JL = ["北千住", "綾瀬", "亀有", "金町"]

station_list = ["北千住", "綾瀬", "亀有", "金町"]

bound_list = ["北千住 以西", "綾瀬", "金町 以東"]


def endstation(b):
    if b == "北千住 以西":
        return "北千住"
    elif b == "金町 以東":
        return "金町"
    return b

def JL_res(crr, b, i):
    e = endstation(b)
    idx_crr = JL.index(crr)
    idx_end = JL.index(e)
    if idx_crr < idx_end:
        return JL[min(idx_crr + i, idx_end)]
    elif idx_end < idx_crr:
        return JL[max(idx_crr - i, idx_end)]
    return crr

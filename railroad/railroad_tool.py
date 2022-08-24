from railroad import jk, jy

def is_station_in_line(cs, l):
    if l == "山手線":
        return cs in jy.JY
    elif l == "京浜東北線(各駅停車)":
        return cs in jk.JK
    elif l == "京浜東北線(快速)":
        return cs in jk.JK_rapid
    
    return False

def next_stop(crr, l, b, i):
    if l == "山手線" and b == "外回り":
        return jy.JY_outer_res(crr, i)
    elif l == "山手線" and b == "内回り":
        return jy.JY_inner_res(crr, i)
    elif l == "京浜東北線(各駅停車)":
        return jk.JK_res(crr, b, i)
    elif l == "京浜東北線(快速)":
        return jk.JK_rapid_res(crr, b, i)

    return -1

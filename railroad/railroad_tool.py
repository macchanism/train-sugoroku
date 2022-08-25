from railroad import jb, jc, je, jk, jy


def is_station_in_line(cs, l):
    if l == "総武線(各駅停車)":
        return cs in jb.JB
    elif l == "中央線(快速)":
        return cs in jc.JC_rapid
    elif l == "中央線(通勤快速)":
        return cs in jc.JC_commuterrapid
    elif l == "中央線(中央・青海特快)":
        return cs in jc.JC_specialrapid
    elif l == "中央線(通勤特快)":
        return cs in jc.JC_commuterspecialrapid
    elif l == "京葉線(各駅停車)":
        return cs in je.JE
    elif l == "京葉線(快速・通勤快速)":
        return cs in je.JE_rapid
    elif l == "京浜東北線(各駅停車)":
        return cs in jk.JK
    elif l == "京浜東北線(快速)":
        return cs in jk.JK_rapid
    elif l == "山手線":
        return cs in jy.JY
    
    return False

def next_stop(crr, l, b, i):
    if l == "総武線(各駅停車)":
        return jb.JB_res(crr, b, i)
    elif l == "中央線(快速)":
        return jc.JC_rapid_res(crr, b, i)
    elif l == "中央線(通勤快速)":
        return jc.JC_commuterrapid_res(crr, b, i)
    elif l == "中央線(中央・青海特快)":
        return jc.JC_specialrapid_res(crr, b, i)
    elif l == "中央線(通勤特快)":
        return jc.JC_commuterspecialrapid_res(crr, b, i)
    elif l == "京葉線(各駅停車)":
        return je.JE_res(crr, b, i)
    elif l == "京葉線(快速・通勤快速)":
        return je.JE_rapid_res(crr, b, i)
    elif l == "京浜東北線(各駅停車)":
        return jk.JK_res(crr, b, i)
    elif l == "京浜東北線(快速)":
        return jk.JK_rapid_res(crr, b, i)
    elif l == "山手線" and b == "外回り":
        return jy.JY_outer_res(crr, i)
    elif l == "山手線" and b == "内回り":
        return jy.JY_inner_res(crr, i)

    return -1

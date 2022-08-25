from railroad import jb, jc, je, jk, js, jy


def is_station_in_line(cs, l):
    if l == "総武線・中央線(各駅停車)":
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
    elif l == "湘南新宿ライン(宇都宮線・横須賀線直通)(普通・快速)":
        return cs in js.JS_U_JO
    elif l == "湘南新宿ライン(高崎線・東海道線直通)(普通・快速)":
        return cs in js.JS_T_JT
    elif l == "湘南新宿ライン(高崎線・東海道線直通)(特別快速)":
        return cs in js.JS_T_JT_specialrapd
    elif l == "山手線":
        return cs in jy.JY

    return False

def next_stop(crr, l, b, i):
    ret = -1
    if l == "総武線・中央線(各駅停車)":
        ret = jb.JB_res(crr, b, i)
    elif l == "中央線(快速)":
        ret = jc.JC_rapid_res(crr, b, i)
    elif l == "中央線(通勤快速)":
        ret = jc.JC_commuterrapid_res(crr, b, i)
    elif l == "中央線(中央・青海特快)":
        ret = jc.JC_specialrapid_res(crr, b, i)
    elif l == "中央線(通勤特快)":
        ret = jc.JC_commuterspecialrapid_res(crr, b, i)
    elif l == "京葉線(各駅停車)":
        ret = je.JE_res(crr, b, i)
    elif l == "京葉線(快速・通勤快速)":
        ret = je.JE_rapid_res(crr, b, i)
    elif l == "京浜東北線(各駅停車)":
        ret = jk.JK_res(crr, b, i)
    elif l == "京浜東北線(快速)":
        ret = jk.JK_rapid_res(crr, b, i)
    elif l == "湘南新宿ライン(宇都宮線・横須賀線直通)(普通・快速)":
        ret = js.JS_U_JO_res(crr, b, i)
    elif l == "湘南新宿ライン(高崎線・東海道線直通)(普通・快速)":
        ret = js.JS_T_JT_res(crr, b, i)
    elif l == "湘南新宿ライン(高崎線・東海道線直通)(特別快速)":
        ret = js.JS_T_JT_specialrapd_res(crr, b, i)
    elif l == "山手線" and b == "外回り":
        ret = jy.JY_outer_res(crr, i)
    elif l == "山手線" and b == "内回り":
        ret = jy.JY_inner_res(crr, i)
    
    if ret == "葛西臨海公園":
        ret += " (Goal!!!)"
    elif ret == crr:
        ret += " (Stay here... Re-choose another train and retry!)"

    return ret

    return ret

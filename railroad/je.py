# 京葉線
JE = ["東京", "八丁堀", "越中島", "潮見", "新木場", "葛西臨海公園"]
JE_rapid = ["東京", "八丁堀", "新木場"]
JE_commuterrapid = JE_rapid

type_list = ["各駅停車", "快速", "通勤快速"]

bound_list = ["東京", "下り方面"]


def JE_res(crr, b, i):
    idx_crr = JE.index(crr)

    if b == "下り方面":
        return JE[min(idx_crr + i, len(JE)-1)]
    elif b == "東京":
        return JE[max(idx_crr - i, 0)]

    return crr

def JE_rapid_res(crr, b, i):
    idx_crr = JE_rapid.index(crr)

    if b == "下り方面":
        return JE_rapid[min(idx_crr + i, len(JE_rapid)-1)]
    elif b == "東京":
        return JE_rapid[max(idx_crr - i, 0)]

    return crr

def JE_commuterrapid_res(crr, b, i):
    idx_crr = JE_commuterrapid.index(crr)

    if b == "下り方面":
        return JE_commuterrapid[min(idx_crr + i, len(JE_commuterrapid)-1)]
    elif b == "東京":
        return JE_commuterrapid[max(idx_crr - i, 0)]

    return crr
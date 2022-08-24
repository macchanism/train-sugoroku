# 京葉線
JE = ["東京", "八丁堀", "越中島", "潮見", "新木場", "葛西臨海公園"]
JE_rapid = ["東京", "八丁堀", "新木場"]


def JE_res(crr, b, i):
    idx_crr = JE.index(crr)

    if b == "京葉線 下り方面":
        return JE[min(idx_crr + i, len(JE)-1)]
    elif b == "東京":
        return JE[max(idx_crr - i, 0)]

    return crr

def JE_rapid_res(crr, b, i):
    idx_crr = JE_rapid.index(crr)

    if b == "京葉線 下り方面":
        return JE_rapid[min(idx_crr + i, len(JE_rapid)-1)]
    elif b == "東京":
        return JE_rapid[max(idx_crr - i, 0)]

    return crr

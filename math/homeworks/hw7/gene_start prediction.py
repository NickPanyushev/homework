def start_pred (TSS, position):
    diff = []
    for i in range(len (TSS)):
        diff.append(abs(TSS[i]-position))
    num = diff.index(min(diff))
    return TSS [num]

print(start_pred([12,21,34,10,2,56], 11))

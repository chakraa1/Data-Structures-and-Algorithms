def cal_sum(N):
    if N == 1:
        return 1
    return N + cal_sum(N-1)
N = 4
print(cal_sum(N))
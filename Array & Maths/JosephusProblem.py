"""
N people standing in the circle and killing each other.
Find the place Josephus should stand at
"""
def FindStandingPlace(N):
    i = 1
    while i <= N:
        i *= 2
    i = i // 2

    killed = N - i

    return 2 * killed + 1
print(FindStandingPlace(100))

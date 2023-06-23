def find_comb(n,k):
    c: list[list[int]] = []
    s: list[int] = []

    def f(i:int) -> None:
        if len(s) == k:
            c.append(s[:])
            return
        if i == n + 1:
            return
        else:
            s.append(i)
            f(i+1)
            s.pop()
            f(i+1)
    f(1)
    return c
n = 4
k=2
print(find_comb(n,k))

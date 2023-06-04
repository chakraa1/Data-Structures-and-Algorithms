def calPow(a,n,p):
    if a == 1 or n == 0:
        return 1
    if n % 2 == 0:
        return (calPow(a,n//2,p)*calPow(a,n//2,p)%p)
    else:
        return (a%p*(calPow(a,n//2,p)*calPow(a,n//2,p)%p))

a = 2
n =3
p = 3
print(calPow(a,n,p))


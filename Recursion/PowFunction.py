def calPow(a,n,p):
    if a == 1 or n == 0:
        return 1
    if n % 2 == 0:
        return (calPow(a,n//2,p)*calPow(a,n//2,p)%p)
    else:
        return (a%p*(calPow(a,n//2,p)*calPow(a,n//2,p)%p))

def calPowOptimal(a,n,p):
    if a == 1 or n == 0:
        return 1
    hp = calPowOptimal(a,n//2,p)
    if n % 2 == 0:
        return (hp*hp)%p
    else:
        return (((hp*hp)%p)*a%p)%p
a = 2
n =3
p = 3
print(calPow(a,n,p))


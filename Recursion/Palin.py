def palin(s):
    n = len(s)
    result = isPalin(s,0, n-1)
    if result == True:
        print("Palindrome")
    else:
        print("Not palindrome")

def isPalin(s,start, end):
    if start >= end:
        return True
    return s[start] == s[end] and isPalin(s,start+1,end -1)
print(palin("NitiNi"))

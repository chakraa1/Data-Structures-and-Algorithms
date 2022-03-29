def StringOperations(A):
    ans = ''
    concatStr = A + A
    chars = list(concatStr)
    for i,char in enumerate(chars):
        code = ord(char)
        if 65 <= code <= 90:
            chars[i] =''

    for i,char in enumerate(chars):
        if char in ('a','e','i','o','u'):
            chars[i] ='#'

    ans += ''.join(chars)
    return ans
A="AbcaZeoB"
print(StringOperations(A))
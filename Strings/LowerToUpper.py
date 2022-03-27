"""
Toggle strings, ignoring special characters
"""
def toggle_case(s):
    letters=list(s)
    print(letters)
    for i,char in enumerate(s):
        code = ord(char)
        if (65 <= code <= 90) or (97 <= code <= 122):
            letters[i] = chr(code ^ 32)

    ans =''.join(letters)

    return ans
s = "I am in Git!"
print(toggle_case(s))
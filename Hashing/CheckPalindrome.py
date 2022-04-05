def checkPalindromePossible(str):
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    # Python program to take multiple inputs from the user
    freq={}
    ans=0
    for char in str:
        if char in freq:
            freq[char] += 1
        else:
            freq[char]= 1
    print(freq)
    odd_frequencies = 0
    for char_freq in freq.values():
        print(" char ",char_freq)
        if char_freq % 2 == 1:
            odd_frequencies += 1
    if odd_frequencies == 1:
        ans=1
    return ans


if __name__ == '__main__':
    A = "axax"
    #A = "abbdcfg"
    print(checkPalindromePossible(A))
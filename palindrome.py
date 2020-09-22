def isValidChar(c):
    return c.isalpha()

def isPalindrome(S):
    start =0
    end = len(S)-1

    while start < end:
        c1 = S[start].lower()
        c2 = S[end].lower()
        if isValidChar(c1) and isValidChar(c2):
            if c1 != c2:
                return False
            start += 1
            end -= 1
        if not isValidChar(c1):
            start += 1
        if not isValidChar(c2):
            end -= 1
    return True




S = "abba"

print(isPalindrome(S))
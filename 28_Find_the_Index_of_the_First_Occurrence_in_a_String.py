haystack = "leetcode"
needle = "leeto"
q = haystack.find(needle)
print(q)

'''
def strStr(haystack, needle):
    n = len(haystack)
    m = len(needle)

    for i in range(n - m + 1):  # loop through possible starting points
        if haystack[i:i+m] == needle:  # check substring of length m
            return i
    return -1
'''

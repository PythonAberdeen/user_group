def isAnagram(string1, string2):
    d = {}
    for c in string1:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    for c in string2:
        if c in d:
            d[c] -= 1
            if d[c] == 0:
                del d[c]
        else:
            return False
    return True


print(isAnagram("listen", "silent"))
print(isAnagram("Netherlands", "Neanderthals"))

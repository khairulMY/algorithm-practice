def is_anagram(s, t):
    if len(s) != len(t):
        return False
    s = sorted(s)
    t = sorted(t)
    return s == t

print(is_anagram("listen", "silent"))   # True
print(is_anagram("rat", "car"))         # False
print(is_anagram("aab", "abb"))         # False
print(is_anagram("", ""))               # True
print(is_anagram("a", "ab"))            # False
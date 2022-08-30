import math
def gcd(s1, s2):
    return s1 + s2 == s2 + s1 and s1[: math.gcd(len(s1), len(s2))] or ''

a = 'ababab'
b = 'ab'
print(gcd(a,b))
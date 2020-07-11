from collections import Counter
def minSteps(s,t):
    diff = Counter(s) - Counter(t)
    return sum(diff.values())

s = "friend"
t = "family"

print(minSteps(s, t))

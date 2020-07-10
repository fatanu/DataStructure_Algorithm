"""
Question:
Check whether two strings are anagram of each other:
Solution: Two possible solution, One in 0(n) and the other in 0(nlogn)

"""
"""
For nlogn solution

"""
def are_anagram1(strg1, strg2):
    if len(strg1) != len(strg2):
        return False
    return sorted(strg1) == sorted(strg2)


def are_anagram2(strg1, strg2):
    if len(strg1) != len(strg2):
        return False

    xor_value = 0
    for i in range(len(strg1)):
        xor_value = xor_value ^ ord(strg1[i])
        xor_value = xor_value ^ ord(strg2[i])

    if xor_value == 0:
        return True
    else:
        return False


print(are_anagram1("", ""))
print(are_anagram2("", ""))




"""
Given an array of strings, group anagrams together
For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"]

Return:
[
 ["ate", "eat", "tea"],
 ["nat", "tan"]
 ["bat"]
]

"""

def grp_anagram(lst):
    anagramMap = {}
    for str in lst:
        sortedStr = "".join(sorted(str))
        if sortedStr not in anagramMap.keys():
            anagramMap[sortedStr] = []
        anagramMap[sortedStr].append(str)
    return list(anagramMap.values())


test = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(grp_anagram(test))



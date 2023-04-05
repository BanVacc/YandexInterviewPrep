def isAnagram(word1: str, word2: str):
    count = dict()
    if len(word1) != len(word2) or len(word1) == 0 or len(word2) == 0:
        return 0

    for i in range(len(word1)):
        s1 = word1[i]
        s2 = word2[i]

        count[s1] = count.get(s1, 0) + 1
        count[s2] = count.get(s2, 0) - 1

    for cnt in count.values():
        if cnt != 0:
            return 0
    return 1


word1 = input()
word2 = input()
print(isAnagram(word1, word2))

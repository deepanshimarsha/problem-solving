class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        telephone = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                     "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        if len(digits) == 0:
            return []
        letter = [""]
        for i in digits:
            # print(i)
            letter = combination(letter, telephone[i])
        return letter


def combination(l1, l2):
    lists = []
    for i in range(0, len(l2)):
        for j in range(0, len(l1)):
            # print(j)
            lists.append(l1[j] + l2[i])

    return lists


def matchingStrings(strings, queries):

    count = {}

    for letters in queries:
        if letters in count:

        count[letters] = 0

    for letters in strings:
        if letters in count:
            count[letters] = count[letters] + 1

    lists = []
    for key in count:
        lists.append(count[key])
        return lists

print(matchingStrings(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc']))

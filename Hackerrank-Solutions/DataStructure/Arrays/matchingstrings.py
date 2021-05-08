def matchingstrings(strings, queries):

    count = 0
    for i in range(0, len(queries)):
        for j in range(0, len(strings)):
            if queries[i] == strings[j]:
                count = count + 1

        print(count)
        count = 0


matchingstrings(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc'])



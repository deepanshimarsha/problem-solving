def consecutive(array):
    j = 0
    for i in range(len(array)):
        count = 0
        i = j
        if i >= len(array):
            break
        j = i + 1

        if array[j] == array[i] + 1:
            print(array[i], end="")
            i = j
            j = i+1
            k = j
            if j < len(array)-1:
                while array[j] == array[i]+1:
                    i = j
                    j = i + 1
                    #print(i)
                    #print(j)
                    #if j >= len(array)-1:
                        #break
            if j == k:
                print(",", end="")
                print(array[i],end=",")

            elif j == len(array)-1:
                #print("-", end="")
                print(array[i])
            else:
                print("-", end="")
                print(array[i], end=",")

        else:
            print(array[i], end=",")
            j = i + 1

consecutive([1,2,5,8,9,10,11,13,14])
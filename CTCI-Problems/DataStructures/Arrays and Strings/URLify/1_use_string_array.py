def URLify(str):
    max = 1000

    #remove leading and trailing spaces
    str = str.strip()

    l = len(str)
    space_count = str.count(" ")

    #calculate the length of str after modification
    new_len = l + space_count * 2

    #new str length shouldnt be greater than max str length given
    if new_len > max:
        return -1

    index = new_len-1

    #make a string array
    str = list(str)

    #extend the array to make its length equal to the new length
    for i in range(new_len-l):
        str.append("0")

    #fill the array from end
    for j in range(l-1, 0, -1):
        #print(j,index)
        if str[j] == " ":
            str[index] = "0"
            str[index-1] = "2"
            str[index-2] = "%"
            index = index - 3
        else:
            str[index] = str[j]
            index = index - 1
    return "".join(str)

print(URLify("Mr John Smith    "))
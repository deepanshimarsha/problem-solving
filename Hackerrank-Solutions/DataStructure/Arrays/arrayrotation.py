def arrayrotation(arr, d):

    rotatedarr = []

    for i in range(d, len(arr)):
        rotatedarr.append(arr[i])

    for i in range(0, d):
        rotatedarr.append(arr[i])

    return rotatedarr

print(arrayrotation([1,2,3,4,5], 4))

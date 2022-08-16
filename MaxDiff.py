def maxDifferenceOddEven(arr):
    result = -1
    length = len(arr)

    for j in range(length):
        right = arr[j]
        for i in range(length):
            if arr[i]<right and right % 2 == 0 and arr[i]%2 == 1:
                diff = right - arr[i]
                if diff > result:
                    result = diff
    return result


list = [1,2,3,6,4]
print(maxDifferenceOddEven(list))
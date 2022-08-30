


def cardinalitySort(nums):
    return sorted(nums, key=lambda x: (bin(x).count('1'), x))
    # note
if __name__ == "__main__":
    arr = [1024,512,256,128,64,32,16,8,4,2,1]
    arr2 = [1,2,3,4,5]
    print(cardinalitySort(arr2))




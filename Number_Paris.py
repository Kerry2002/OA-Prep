# 双指针思路1 - 只能print一组结果
# def number_pairs(n,k):
#     i,j = 0, len(n)-1
#     list = []
#     while (i<j):
#         result = n[i]+n[j]
#         if result == k:
#             list.append(n[i])
#             list.append(n[j])
#             return list
#         elif result > k:
#             j-=1
#         else: i+=1
#     return None

# 双指针思路2
def number_pairs(n,k):
    arr = len(n)
    result = []
    for i in range(arr):
        for j in range(i+1,arr):
            if n[i]+n[j] == k:
                result.append((n[i],n[j]))
    return result

n = [1,2,3,4,6]
k = 5
print(number_pairs(n,k))


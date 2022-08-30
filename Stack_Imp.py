def stack_Implement(List):
    List.reverse()
    list_result = []
    n = len(List)
    for num in range (n):
        if num % 2 != 0:
            continue
        list_result.append(List[num])
    return list_result


# list = [1,2,3,4]
list = [10,-2,3,4]
print(stack_Implement(list))
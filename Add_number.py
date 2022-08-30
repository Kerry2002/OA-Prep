import sys

# for line in sys.stdin:
#     print(line, end='')

def add_number (number):
    if number <0: return None
    result = 0
    for num in range (number+1):
        if num % 5 == 0 or num % 7 == 0:
            continue
        result = result +num
    return result

print(add_number(10))


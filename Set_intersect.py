import json


# input = '1,2,3,4;4,5,6'
input = '7,8,9;8,9,10,11,12'
a,b = (input.split(';',1))
a = set(a.split(','))
b = set(b.split(','))
print(a.intersection(b))
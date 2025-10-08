from array import array
from my_string import MyString

def collection3(objects: list[MyString]):
    print('\nArray')
    arr = array('i', [s.length for s in objects])

    arr.append(10)
    arr.pop(2)
    arr[0] = 99
    print('Is there 99 in array?', 99 in arr)

    for a in arr:
        print(a)

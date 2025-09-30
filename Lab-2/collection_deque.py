from collections import deque
from my_string import MyString

def collection2(objects: list[MyString]):
    print('\n Non-generic deque')
    d = deque(objects)

    d.append(MyString("is delicious"))
    d.appendleft(MyString("Delicious")) 
    d.pop()
    d.popleft()

    if any(s.value == "Apple" for s in d):
        print("The element 'Apple' is found")
    else:
        print("No such element")

    d[1] = MyString("Dragon fruit")

    for item in d:
        print(item)

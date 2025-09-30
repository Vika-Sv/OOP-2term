from my_string import MyString
from collections import deque
import array

def collection():
    s1 = MyString("Banana")
    s2 = MyString("Peach")
    s3 = MyString("Strowbarry")
    s4 = MyString("Grape")
    s5 = MyString("Apple")

    print("\n Non-generic")
    my_list = [s1, s2, s3]
    my_list.append(s4)           # додавання
    my_list[1] = s5              # оновлення
    del my_list[0]               # видалення
    for obj in my_list:          # обхід
        print(obj)

    print("\n Generic collection")
    my_deque = deque([s1, s2, s3])
    my_deque.append(s4)
    my_deque.popleft()  
    for obj in my_deque:
        print(obj)

    print("\n array")
    my_array = array.array('i', [s1.length, s2.length, s3.length])
    my_array.append(s4.length)  
    my_array[0] = 99            
    print("Array:", list(my_array))

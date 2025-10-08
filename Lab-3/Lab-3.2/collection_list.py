from my_string import MyString

def collection(objects: list[MyString]):
    print('\nGeneric list')
    
    lst = list(objects)
    lst.append(MyString('is delicious'))
    del lst[3]
    lst[3] = MyString('Peach')
    found = any('Banana' in s.value for s in lst)
    print('Found Banana?', found)

    for item in lst:
        print(item)

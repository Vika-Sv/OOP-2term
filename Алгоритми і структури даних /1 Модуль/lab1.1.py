from vectorlist import VectorList
from node import _Node
from node import LinkedStack


def main():
    list1 = VectorList(12)
    stack = LinkedStack()
 
    values = [15, 63, 42, 71, 8, 99, 50, 57, 100, 33, 81, 4]
    for v in values:
        list1.add(v)
 
    print("Початковий стан списку: ", end="")
    list1.print()
 
    print()
 
    i = 0
    while i < list1.size():
        val = list1.get(i)
        if val % 2 != 0 and val > 50:
            list1.remove(i)   
            stack.push(val)
        else:
            i += 1
 
    print()
    print("Перша структура  — ", end="")
    list1.print()
    print("Друга структура  — ", end="")
    stack.print()
 
 
if __name__ == "__main__":
    main()
from my_string import MyString
from collection_list import collection
from collection_deque import collection2
from collection_array import collection3
from binary_tree import BinaryTree

def main():
    s1 = MyString("Apple")
    s2 = MyString("Banana")
    s3 = MyString("Cherry")
    s4 = MyString("Pineapple")
    s5 = MyString("Grape")

    objs = [s1, s2, s3, s4, s5]


    collection(objs)
    collection2(objs)
    collection3(objs)


    print("\n Binary Tree сreated with elements Cherry, Apple, Banana, Grape, Pineapple")
    bt = BinaryTree()
    for obj in [s3, s1, s2, s5, s4]:  
        bt.insert(obj)

if __name__ == "__main__":
    main()

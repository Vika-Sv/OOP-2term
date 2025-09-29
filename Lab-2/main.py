from my_string import MyString
from collection import collection
from binary_tree import BinaryTree

if __name__ == "__main__":
    print("--- Робота з класом MyString ---")
    s = MyString("Hello World")
    print("Рядок:", s)
    print("Пошук 'World':", s.find_substring("World"))
    s.insert_substring(" Python", 5)
    print("Після вставки:", s)
    s.replace_substring("World", "Everyone")
    print("Після заміни:", s)

    
    collection()


    print("\n Binary Tree")
    tree = BinaryTree()
    tree.insert("Banana")
    tree.insert("Peach")
    tree.insert("Strowberry")
    tree.insert("Grape")
    tree.insert("Apple")

    print("inorder:")
    tree.inorder(tree.root)

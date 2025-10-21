from string_class import MyString
import serialization_collections as sc

    
if __name__ == "__main__":
    arr = [
        MyString("Apple"),
        MyString("Banana"),
        MyString("Cherry"),
        MyString("Pineapple"),
        MyString("Grape")
 ]

    print("=== Початковий масив ===")
    for obj in arr:
        print(obj)

    # 2. JSON серіалізація
    sc.save_json("strings.json", arr)
    restored_json = sc.load_json("strings.json")
    print("\n=== JSON десеріалізація ===")
    for obj in restored_json:
        print(obj)

    # 3. Binary серіалізація
    sc.save_binary("strings.bin", arr)
    restored_bin = sc.load_binary("strings.bin")
    print("\n=== Binary десеріалізація ===")
    for obj in restored_bin:
        print(obj)

    # 4. XML серіалізація
    sc.save_xml("strings.xml", arr)
    restored_xml = sc.load_xml("strings.xml")
    print("\n=== XML десеріалізація ===")
    for obj in restored_xml:
        print(obj)

    # 5. Custom серіалізація
    sc.save_custom("strings.txt", arr)
    restored_custom = sc.load_custom("strings.txt")
    print("\n=== Custom десеріалізація ===")
    for obj in restored_custom:
        print(obj)

    # 6. Порівняння масиву і колекції (списку Python)
    print("\n=== Колекція (list) ===")
    collection = [MyString("Колекція1"), MyString("Колекція2")]
    sc.save_json("collection.json", collection)
    restored_col = sc.load_json("collection.json")
    for obj in restored_col:
        print(obj)

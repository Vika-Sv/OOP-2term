from my_string import MyString
import serialization_collections as sc

    
if __name__ == "__main__":
    arr = [
        MyString("Apple"),
        MyString("Banana"),
        MyString("Cherry"),
        MyString("Pineapple"),
        MyString("Grape")
 ]

    # 2. JSON серіалізація
    sc.save_json("strings.json", arr)
    restored_json = sc.load_json("strings.json")
    

    # 3. Binary серіалізація
    sc.save_binary("strings.bin", arr)
    restored_bin = sc.load_binary("strings.bin")
    

    # 4. XML серіалізація
    sc.save_xml("strings.xml", arr)
    restored_xml = sc.load_xml("strings.xml")


    # 5. Custom серіалізація
    sc.save_custom("strings.txt", arr)
    restored_custom = sc.load_custom("strings.txt")

    my_list = [
        MyString("Cucumber"),
        MyString("Carrot"),
        MyString("Potato"),
        MyString("Sweet Peper"),
        MyString("Onion")
    ]


    sc.save_list("list.json", my_list)
    restored_list = sc.load_list("list.json")
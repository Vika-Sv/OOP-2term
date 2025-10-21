import json
import pickle
import xml.etree.ElementTree as ET
from string_class import MyString


def save_json(filename, objects):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([obj.to_dict() for obj in objects], f, ensure_ascii=False, indent=4)

def load_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [MyString.from_dict(d) for d in data]


def save_binary(filename, objects):
    with open(filename, "wb") as f:
        pickle.dump(objects, f)

def load_binary(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)


def save_xml(filename, objects):
    root = ET.Element("Strings")
    for obj in objects:
        elem = ET.SubElement(root, "MyString")
        ET.SubElement(elem, "value").text = obj.value
        ET.SubElement(elem, "length").text = str(obj.length)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def load_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    objects = []
    for elem in root.findall("MyString"):
        value = elem.find("value").text
        objects.append(MyString(value))
    return objects


def save_custom(filename, objects):
    with open(filename, "w", encoding="utf-8") as f:
        for obj in objects:
            f.write(f"{obj.value}|{obj.length}\n")

def load_custom(filename):
    objects = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            value, length = line.strip().split("|")
            objects.append(MyString(value))
    return objects

import xml.etree.ElementTree as et


tree = et.parse('config.xml')
root = tree.getroot()

print(root.tag)
for item in root:
    print(item.tag, item.attrib)
    for child in item:
        print(child.tag + " is: " + child.text)

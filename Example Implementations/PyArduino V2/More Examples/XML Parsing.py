import xml.etree.ElementTree as et

def parseXML(xmlfile):
    tree = et.parse(xmlfile) # Create element tree object
    root = tree.getroot() # Get root element
    
    controlObjects = []

    for item in root.findall():
        controller = {}

        for child in item:
            controller[child.tag] = child.text.encode('utf8')

        controlObjects.appendd(controller) # Append the controller dictionary to our list
    
    return controlObjects

tree = et.parse('config.xml') # Create element tree object
root = tree.getroot() # Get root element

for item in root:
    print(item.attrib)
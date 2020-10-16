#by Aimar Roosalu 09/2020
#Tutorial: https://stackabuse.com/reading-and-writing-xml-files-in-python/
#XML Library document: https://docs.python.org/2/library/xml.etree.elementtree.html#modifying-an-xml-file

import xml.etree.ElementTree as ET
import csv

# create the file structure for adding into file

reader = csv.reader(open('andmed.csv'), delimiter=';') #avame CSV faili, et lugeda kirjeid

data = ET.Element('importRequest') #root element

for row in reader:
    items = ET.SubElement(data, 'assetInput')
    externalId = ET.SubElement(items, 'externalId')
    serialNumber = ET.SubElement(items, 'serialNumber')
    Mark = ET.SubElement(items, 'mark')
    Model = ET.SubElement(items, 'model')
    Year = ET.SubElement(items, 'year')
    description = ET.SubElement(items, 'description')
    contractDate = ET.SubElement(items, 'contractDate')
#    item1.set('type','string')
#    item2.set('type','string')
#    item3.set('type','int')
    externalId.text = row[0]
    serialNumber.text = row[1]
    Mark.text = row[2]
    Model.text = row[3]
    Year.text = row[4]
    description.text = row[5]
    contractDate.text = row[6]
    
# create a new XML file with the results
mydata = ET.tostring(data)

f = open("report.xml", "wb") #avan faili, wb et oleks binary
first_line = '<?xml version="1.0" encoding="utf-8"?>' #lisan faili esimese rea (on string)
f.write(first_line.encode()) #stringi encoding binaryks

f.write(mydata)
f.close()

#test
tree = ET.parse('report.xml')
root = tree.getroot()
print("root: ", root)
print("child: ", root[0][0])
print("child attrib: ", root[0][0].attrib)
print("text:", root[0][0].text)

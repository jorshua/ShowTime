from download import Download
from parse import Parse
from item import Item
import xml.etree.ElementTree as ET

url = 'http://showrss.info/feeds/1166.rss'
#path = '1166.rss'

src = Download.read_content('test.xml')
#Download.save_file(url, 'test2.xml')
#print(src)
l = Parse.parse_content(src)

for x in l:
	print(x)

#root = ET.fromstring(src)
#print([x for x in [child for child in root.iter('item')]])

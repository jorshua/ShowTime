import xml.etree.ElementTree as ET
from item import Item


# TODO -> Exception handling for XML parsing
class Parse:

    """ """

    def __init__(self):
    	pass    

    @staticmethod
    def parse_content(content):
        """Parse RSS file"""
        root = ET.fromstring(content)
        
        nameSpaces = parse_namespaces(root)
        
        return [Parse.parse_item(item, nameSpaces) 
            for item in root.iter('item')]

    @staticmethod
    def parse_namespaces(root):
        """Parse RSS namespaces from root node"""
        return {'showrss': 'http://showrss.info/'}

    @staticmethod
    def parse_item(item, nameSpaces):
        """Parse RSS item"""
        try:
            return Item(item.find('title').text,
                item.find('link').text,
                item.find('pubDate').text,
                item.find('showrss:showid', nameSpaces).text,
                item.find('showrss:showname', nameSpaces).text,
                item.find('enclosure').attrib['url'],
                ' ') #quality
        except AttributeError as ex:
        	print('ERROR: AttributeError exception ->' +\
        		'{0}'.format(ex))
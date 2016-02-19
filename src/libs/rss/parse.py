import xml.etree.ElementTree as ET
from item import Item

class Parse:

    """ """

    ns = {'showrss': 'http://showrss.info/'}

    def __init__(self):
    	pass    

    @classmethod
    def parse_content(self, content):
        """Parse RSS file"""
        root = ET.fromstring(content)
        return [Parse.parse_item(item) for item in root.iter('item')]

    @classmethod
    def parse_item(self, item):
        """Parse RSS item"""
        try:
            return Item(item.find('title').text,
                item.find('link').text,
                item.find('pubDate').text,
                item.find('showrss:showid', self.ns).text,
                item.find('showrss:showname', self.ns).text,
                item.find('enclosure').text,
                ' ') #quality
        except AttributeError as ex:
        	print('ERROR: AttributeError exception ->' +\
        		'{0}'.format(ex))
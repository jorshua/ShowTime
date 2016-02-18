from urllib.request import urlopen


class Download:

    """ """

    def __init__(self):
        pass

    @classmethod
    def save_file(self, url, path):
        """Downloads and saves RSS url to provided path"""
        #url = 'http://showrss.info/feeds/1166.rss'
        #path = '1166.rss'
        response = urlopen(url)
        with open(path, 'wb') as file:
            file.write(response.read())
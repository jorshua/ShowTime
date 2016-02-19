from urllib.request import urlopen


class Download:

    """ """

    def __init__(self):
        pass

    @classmethod
    def get_content(self, url):
        """Get RSS url content"""
        return urlopen(url).read()

    @classmethod
    def save_file(self, url, path):
        """Downloads and saves RSS url to provided path"""
        response = Download.get_content(url)
        with open(path, 'wb') as file:
            file.write(response)

    @classmethod
    def save_content(self, content, path):
        """Saves RSS content to provided path"""
        with open(path, 'wb') as file:
            file.write(content)

    @classmethod
    def read_content(self, path):
        """Saves RSS content to provided path"""
        content = ''
        with open(path, 'r') as file:
            content = file.read()
        return content
from urllib.request import urlopen


# TODO -> Exception handling for file and get operations
class Download:

    """ """

    def __init__(self):
        pass

    @staticmethod
    def get_content(url):
        """Get RSS url content"""
        return urlopen(url).read()

    @staticmethod
    def save_file(url, path):
        """Downloads and saves RSS url to provided path"""
        response = Download.get_content(url)
        with open(path, 'wb') as file:
            file.write(response)

    @staticmethod
    def save_content(content, path):
        """Saves content to file at provided path"""
        with open(path, 'wb') as file:
            file.write(content)

    @staticmethod
    def read_content(path):
        """Saves RSS content to provided path"""
        content = ''
        with open(path, 'r') as file:
            content = file.read()
        return content
from download import Download:


# TODO -> Exception handling for JSON serialization and de-serialization
# -> Better JSON decoder
class Item:

    """ """

    def __init__(self, title, link, publicationDate, showId, showName,
            enclosure, quality):
        self.title = title
        self.link = link
        self.publicationDate = publicationDate
        self.showId = showId
        self.showName = showName
        self.enclosure = enclosure
        self.quality = quality

    def __str__(self):
        return 'Title : ' + self.title + ' \n' +\
            'Link : ' + self.link + ' \n' +\
            'Publication Date : ' + self.publicationDate + ' \n' +\
            'Show Id : ' + str(self.showId) + ' \n' +\
            'Show Name : ' + str(self.showName) + ' \n' +\
            'Enclosure : ' + str(self.enclosure) + ' \n' +\
            'Quality : ' + str(self.quality) + ' \n============'

    @staticmethod
    def save_as_json(nodes, path):
        """Save list of nodes to file as json"""
        json_object = json.dumps(a.__dict__, 
            sort_keys=True, indent=4, separators=(',',': '))
        Download.save_content(json_object, path)

    @staticmethod
    def read_from_json(path):
        """Read list of nodes from file as json"""
        def object_decoder(json_object):
            if 'title' in json_object and
               'link' in json_object and
               'publicationDate' in json_object and
               'showId' in json_object and
               'showName' in json_object and
               'enclosure' in json_object and
               'quality' in json_object:
                return Item(json_object['title'], 
                            json_object['link'],
                            json_object['publicationDate'],
                            json_object['showId'],
                            json_object['showName'],
                            json_object['enclosure'],
                            json_object['quality'])
            return json_object
        json_object = Download.read_content(path)
        return json.loads(json_object, object_hook=object_decoder)

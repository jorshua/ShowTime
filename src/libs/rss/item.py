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
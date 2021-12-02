class Track(object):
    name: str
    artists: [str]
    id: str

    def __init__(self, name: str, artists: [str], id: str = None):
        self.name = name
        self.artists = artists
        self.id = id

    def __str__(self):
        string = self.name

        for artist in self.artists:
            string += f' {artist}'

        return string

    @property
    def id(self):
        return f'spotify:track:{self._id}'

    @id.setter
    def id(self, value):
        self._id = value

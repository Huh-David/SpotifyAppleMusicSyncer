class Track(object):
    name: str
    artists: [str]

    def __init__(self, name: str, artists: [str]):
        self.name = name
        self.artists = artists

    def __str__(self):
        string = self.name

        for artist in self.artists:
            string += f' {artist}'

        return string

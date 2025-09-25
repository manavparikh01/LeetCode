class Codec:

    def __init__(self):
        self.length = 1
        self.encodemap = {}
        self.decodemap = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.encodemap[longUrl] = self.length
        self.decodemap[self.length] = longUrl
        return self.length
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decodemap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
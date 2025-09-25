class Codec:

    def __init__(self):
        self.length = 1
        self.encodemap = {}
        self.decodemap = {}
        self.base = "https://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encodemap:
            shorturl = self.base + str(self.length)
            self.encodemap[longUrl] = shorturl
            self.decodemap[shorturl] = longUrl
        return self.encodemap[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decodemap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
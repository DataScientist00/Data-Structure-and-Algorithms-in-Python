#problem link-->> https://leetcode.com/problems/encode-and-decode-tinyurl/

class Codec:

    def __init__(self):
        self.encode1 = {}
        self.decode1 = {}
        self.baseurl = "https://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encode1:
            shortUrl = self.baseurl + str(len(self.encode1) + 1)
            self.encode1[longUrl] = shortUrl
            self.decode1[shortUrl] = longUrl
        return self.encode1[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decode1[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

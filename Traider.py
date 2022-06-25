from Marketplace import Marketplase

class Tr(Marketplase):


    def __init__(self, text, name, url):
        super().__init__(name, url)
        self.mytext = text

    def pasrsing(self):
        print("i'm from Traiding class" + self.mytext)
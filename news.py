class News:

    def __init__(self, link, title, img, content):
        self.link = link
        self.title = title
        self.img = img
        self.content = content


    def create_text(self):
        txt = 'Title : {} \nLink : {} \nContent : {}'.format(self.title, self.link, self.content)
        return txt.encode('latin-1', 'replace').decode('latin-1')    
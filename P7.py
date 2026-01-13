class TagClass:
    def __init__(self, txt):
        self.txt = txt
        self.tag = ""
    
    def display(self):
        wrapped_txt = f"<{self.tag}>{self.txt}</{self.tag}>"
        return wrapped_txt

class Paragraph(TagClass):
    def __init__(self, txt):
        super().__init__(txt)
        self.tag = "p"
    
class Lists(TagClass):
    def __init__(self, txt):
        super().__init__(txt)
        self.tag = "li"


ob2 = Paragraph("test for a paragraph")
print(ob2.display())
ob3 = Lists("txts for a list")
print(ob3.display())

#Function version:

def Tag(txt, tag):
    print(f"<{tag}>{txt}</{tag}>")

Tag(txt="For paragraph", tag="p")
Tag(txt="For list", tag="li")

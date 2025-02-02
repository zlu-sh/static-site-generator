from enum import Enum

class TextType(Enum):
    NORMAL = ""
    BOLD = "bold"
    ITALIC = ""
    CODE = ""
    LINK = ""
    IMAGE = ""


class TextNode:
    def __init__(self, text, text_type, url=None):
        if not isinstance(text_type, TextType):
            raise ValueError("text_type must be a TextType enum")
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self == other

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url}"

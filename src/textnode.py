from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        if not isinstance(text_type, TextType):
            raise ValueError("text_type must be a TextType enum")
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
                self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url}"

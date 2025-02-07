from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Must have a tag")
        if self.children == None:
            raise ValueError("Must have children")

        html_string = ""
        for child in self.children:
            html_string += child.to_html()
        return f"<{self.tag}>{html_string}</{self.tag}>"

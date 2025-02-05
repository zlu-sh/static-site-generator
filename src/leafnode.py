from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None or self.tag == "":
            return str(self.value)
        if self.tag == "p":
            return f"<p>{self.value}</p>"
        if self.tag == "a":
            return f"<a super().props_to_html()>self.value</a>"

        def __repr__(self):
            return f"LeafNode({self.tag}, {self.value}, {self.props})"

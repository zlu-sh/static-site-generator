from textnode import TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None,text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": f"{text_node.url}", "alt": f"{text_node.text}"})

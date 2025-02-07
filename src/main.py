from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
    print(TextNode("some_shit", TextType.BOLD, "hhttttt"))
    print(HTMLNode("tag", "value", "children", "prop"))
    print(LeafNode("p", "Paragraph"))
    print(LeafNode("a", "Click me", {"href": "https://google.com"}))

    node1 = LeafNode("p", "Paragraph", {"style": "color:blue;size:16;"})
    node2 = LeafNode("a", "Click this", {"href": "https://google.com", "style": "color:red;"})
    html1 = node1.to_html()
    html2 = node2.to_html()
    print(html1)
    print(html2)

main()

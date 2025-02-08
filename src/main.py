from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from node_conversion import text_node_to_html_node, extract_markdown_images
from node_split import split_nodes_delimiter

def main():
    print(TextNode("some_shit", TextType.BOLD, "hhttttt"))
    print(HTMLNode("tag", "value", "children", "prop"))
    print(LeafNode("p", "Paragraph"))
    print(LeafNode("a", "Click me", {"href": "https://google.com"}))

    node1 = LeafNode("p", "Paragraph", {"style": "color:blue;size:16;"})
    node2 = LeafNode("a", "Click this", {"href": "https://google.com", "style": "color:red;"})
    node3 = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    html1 = node1.to_html()
    html2 = node2.to_html()
    html3 = node3.to_html()
    print(html1)
    print(html2)
    print(html3)

    node = TextNode("Hello `world` today", TextType.TEXT)
    result = split_nodes_delimiter([node], "`", TextType.CODE)
    # Should give you 3 nodes: "Hello ", "world", " today"
    print(result)

    extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
main()

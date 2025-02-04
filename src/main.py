from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    print(TextNode("some_shit", TextType.BOLD, "hhttttt"))
    print(HTMLNode("tag", "value", "children", "prop"))
    

main()

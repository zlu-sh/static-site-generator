import unittest
from node_conversion import text_node_to_html_node
from textnode import TextNode, TextType

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_empty_text(self):
        node = TextNode("", TextType.TEXT) # Create a node with empty text
        result = text_node_to_html_node(node) # Turn that text node into an html node
        self.assertEqual(result.value, "") # Check to see if the text of html node is empty text

    def test_is_bold(self):
        node = TextNode("Text", TextType.BOLD)
        result = text_node_to_html_node(node)
        self.assertEqual(result.tag, "b")

    def test_is_italic(self):
        node = TextNode("Text", TextType.ITALIC)
        result = text_node_to_html_node(node)
        self.assertEqual(result.tag, "i")

    def test_is_code(self):
        node = TextNode("Text", TextType.CODE)
        result = text_node_to_html_node(node)
        self.assertEqual(result.tag, "code")

    def test_is_link(self):
        node = TextNode("Text", TextType.LINK, "https://zlu.sh/")
        result = text_node_to_html_node(node)
        self.assertEqual(result.tag, "aa")

    def test_link_has_url(self):
        url = "https://zlu.sh/"
        node = TextNode("Text", TextType.LINK, url)
        result = text_node_to_html_node(node)
        self.assertEqual(result.props["href"], url)

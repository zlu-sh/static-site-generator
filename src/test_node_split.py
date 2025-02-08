import unittest
from textnode import TextType, TextNode
from node_split import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("Hello `world` today", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result[1].text_type, TextType.CODE)

    def test_bold(self):
        node = TextNode("Hello *world* today", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(result[1].text_type, TextType.BOLD)

    def test_italic(self):
        node = TextNode("Hello **world** today", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.ITALIC)
        self.assertEqual(result[1].text_type, TextType.ITALIC)

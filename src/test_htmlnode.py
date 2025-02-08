import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node1, node2)

    def test_no_tag(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)

    def test_no_value(self):
        node = HTMLNode()
        self.assertIsNone(node.value)

    def test_no_children(self):
        node = HTMLNode()
        self.assertIsNone(node.children)

    def test_no_props(self):
        node = HTMLNode()
        self.assertIsNone(node.props)

    def test_eq_tag(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node1.tag, node2.tag)

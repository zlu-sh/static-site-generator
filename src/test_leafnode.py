import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "Paragraph")
        node2 = LeafNode("p", "Paragraph")
        self.assertEqual(node, node2)

    def test_diff_type(self):
        node = LeafNode("p", "Paragraph")
        node2 = LeafNode("a", "link", {"href": "https://google.com"})
        self.assertNotEqual(node.tag, node2.tag)

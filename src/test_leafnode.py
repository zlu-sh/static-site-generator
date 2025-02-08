import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "Paragraph")
        node2 = LeafNode("p", "Paragraph")
        self.assertEqual(node, node2)

    def test_diff_type(self):
        node = LeafNode("p", "Paragraph")
        node2 = LeafNode("a", "link", {"href": "https://zlu.sh/"})
        self.assertNotEqual(node.tag, node2.tag)

    def test_paragraph_node(self):
        node = LeafNode("p", "Paragraph", {"style": "color:red;"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Paragraph")
        self.assertEqual(node.props["style"], "color:red;")

    def test_link_node(self):
        node = LeafNode("a", "link", {"href": "https://zlu.sh/"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "link")
        self.assertEqual(node.props["href"], "https://zlu.sh/")

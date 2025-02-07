import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_basic_parent_node(self):
        node = ParentNode("div", [LeafNode(None, "text")])
        assert node.to_html() == "<div>text</div>"

    def test_nested_nodes(self):
        inner = ParentNode("p", [LeafNode("b", "bold")])
        outer = ParentNode("div", [inner])
        assert outer.to_html() == "<div><p><b>bold</b></p></div>"

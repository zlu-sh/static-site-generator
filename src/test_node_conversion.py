import unittest
from node_conversion import text_node_to_html_node, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_empty_text(self):
        node = TextNode("", TextType.TEXT) # Create a node with empty text
        result = text_node_to_html_node(node) # Turn that text node into an html node
        self.assertEqual(result.value, "") # Check to see if the text of html node is empty text

    def test_bold_node(self):
        node = TextNode("text", TextType.BOLD)
        result = text_node_to_html_node(node)
        self.assertEqual(result.tag, "b")
        self.assertEqual(result.value, "text")

    def test_italic_node(self):
        node = TextNode("text", TextType.ITALIC)
        result = text_node_to_html_node(node)
        self.assertEqual(result.tag, "i")
        self.assertEqual(result.value, "text")

    def test_code_node(self):
        node = TextNode("text", TextType.CODE)
        result = text_node_to_html_node(node)
        self.assertEqual(result.tag, "code")
        self.assertEqual(result.value, "text")

    def test_link_node(self):
        url = "https://zlu.sh"
        node = TextNode("text", TextType.LINK, url)
        result = text_node_to_html_node(node)

        self.assertEqual(result.tag, "a")
        self.assertEqual(result.value, "text")
        self.assertEqual(result.props["href"], url)

    def test_image_node(self):
        alt_text = "alt text"
        src_url = "./img.png"
        node = TextNode(alt_text, TextType.IMAGE, src_url)
        result = text_node_to_html_node(node)

        self.assertEqual(result.tag, "img")
        self.assertEqual(result.props["src"], src_url)
        self.assertEqual(result.props["alt"], alt_text)

    def test_invalid_text_type(self):
        node = TextNode("text", "not_a_valid_type")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

class TestExtractMarkdownImages(unittest.TestCase):
    def test_result(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        self.assertEqual(result[0], ("rick roll", "https://i.imgur.com/aKaOqIh.gif"))
        self.assertEqual(result[1], ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"))

    def test_no_text(self):
        text = ""
        result = extract_markdown_images(text)
        self.assertEqual(result, [])

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_result(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        self.assertEqual(result[0], ("to boot dev", "https://www.boot.dev"))
        self.assertEqual(result[1], ("to youtube", "https://www.youtube.com/@bootdotdev"))

    def test_no_text(self):
        text = ""
        result = extract_markdown_images(text)
        self.assertEqual(result, [])

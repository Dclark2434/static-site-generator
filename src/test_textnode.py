import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

class TextLinkNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a link node", TextType.TEXT, "https://www.google.com")
        node2 = TextNode("This is a link node", TextType.TEXT, "https://www.google.com")
        self.assertEqual(node, node2)

class TextNoneURLNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a link node", TextType.TEXT, None)
        node2 = TextNode("This is a link node", TextType.TEXT)
        self.assertEqual(node, node2)

class TestDiffNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text nodes", TextType.TEXT)
        node2 = TextNode("This is a text nodes", TextType.BOLD)
        self.assertNotEqual(node, node2)

class TestText(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

class TestCode(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is supposed to be code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is supposed to be code")

class TestBold(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is supposed to be bolded", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is supposed to be bolded")

class TestImage(unittest.TestCase):
    def test_image_with_url(self):
        node = TextNode("An image description", TextType.IMAGE, url="https://google.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://google.com/image.png", "alt": "An image description"})

    def test_image_without_url(self):
        node = TextNode("Image without a URL", TextType.IMAGE)
        with self.assertRaises(ValueError) as context:
            text_node_to_html_node(node)
        self.assertEqual(str(context.exception), "URL must be provided for an image text type")

if __name__ == "__main__":
    unittest.main()
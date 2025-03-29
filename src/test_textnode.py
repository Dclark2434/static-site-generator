import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()
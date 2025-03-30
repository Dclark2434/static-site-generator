import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_attributes(self):
        node = LeafNode("a", "Click me!", {"href": "https://example.com"})
        self.assertEqual(
            node.to_html(), 
            '<a href="https://example.com">Click me!</a>'
        )

    def test_to_html_no_attributes(self):
        node = LeafNode("p", "Hello, world!", {})
        self.assertEqual(
            node.to_html(), 
            '<p>Hello, world!</p>'
        )

    def test_to_html_no_tag_but_value(self):
        node = LeafNode(None, "Just text", None)
        self.assertEqual(
            node.to_html(),
            "Just text"
        )

    def test_to_html_raises_value_error(self):
        with self.assertRaises(ValueError):
            node = LeafNode("div", "", {})
            node.to_html()

    def test_to_html_raises_value_error_with_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("div", None, {})
            node.to_html()
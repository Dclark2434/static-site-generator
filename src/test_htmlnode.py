import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {"href": "https://example.com", "target": "_blank"}
        node = HTMLNode(tag="a", props=props)
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode(tag="p", value="Hello, world!")
        self.assertEqual(
            repr(node),
            "HTMLNode(tag=p, value=Hello, world!, children=[], props={})"
        )

    def test_nodes(self):
        node = HTMLNode()
        self.assertEqual(repr(node), "HTMLNode(tag=None, value=None, children=[], props={})")

    def test_nodes_with_args(self):
        node = HTMLNode(tag="div", value="Hello", children=[HTMLNode("p")], props={"class": "test"})
        self.assertEqual(
            repr(node),
            "HTMLNode(tag=div, value=Hello, children=[HTMLNode(tag=p, value=None, children=[], props={})], props={'class': 'test'})"
        )
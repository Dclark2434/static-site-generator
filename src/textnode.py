from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        if url == "":
            url = None
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.type is TextType.BOLD:
        bold_node = LeafNode("b", text_node.text)
        return bold_node
    elif text_node.type is TextType.TEXT:
        plain_node = LeafNode(None, text_node.text)
        return plain_node
    elif text_node.type is TextType.ITALIC:
        italic_node = LeafNode("i", text_node.text)
        return italic_node
    elif text_node.type is TextType.CODE:
        code_node = LeafNode("code", text_node.text)
        return code_node
    elif text_node.type is TextType.LINK:
        if text_node.url:
            link_node = LeafNode("a", text_node.text, {"href": text_node.url})
            return link_node
        else:
            raise ValueError("URL must be provided for a link text type")
    elif text_node.type is TextType.IMAGE:
        if text_node.url:
            image_node = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
            return image_node
        else:
            raise ValueError("URL must be provided for an image text type")
    else:
        raise ValueError(f"Unsupported text type: {text_node.type}")
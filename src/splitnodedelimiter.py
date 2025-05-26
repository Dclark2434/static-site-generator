from textnode import TextNode
from textnode import TextType

def split_nodes_delimiter(old_nodes, delimiter, new_text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = node.content.split(delimiter)
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    if part:
                        new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    if part:
                        new_nodes.append(TextNode(part, new_text_type))
        else:
            new_nodes.append(node)
    return new_nodes
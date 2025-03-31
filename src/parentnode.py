from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None or tag == "":
            raise ValueError("tag is required for ParentNode")
        if children is None:
            raise ValueError("children is required for ParentNode")
        if not isinstance(children, list):
            raise TypeError("children must be a list")
        
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None or self.tag == "":
            raise ValueError("tag is required for ParentNode")
        if self.children is None:
            raise ValueError("children is required for ParentNode")
    
        child_html = ""
        for child in self.children:
            child_html += child.to_html()

        return f"<{self.tag}>{child_html}</{self.tag}>"
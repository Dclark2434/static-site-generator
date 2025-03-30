class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError(
            "The method to_html() is not implemented in HTMLNode."
            "Was this intended to be for a LeafNode?"
        )
    
    def props_to_html(self):
        return " " + " ".join(f'{key}="{value}"' for key, value in (self.props or {}).items())
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

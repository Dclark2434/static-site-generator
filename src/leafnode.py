from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        super().__init__(tag, children=[], props=props)
        self.value = value
        # so I found that in python if you explicity set an argument like children 
        # is, then the following position arguments NEED to be explicityly stated.
        # This is why props=props but tag can just be left as is.

    def to_html(self):
        if self.value is None or self.value == "":
            raise ValueError("LeafNode has no value")
        if self.tag is None or self.tag == "":
            return self.value
        # builds the attributes string
        attrs = " ".join(f'{key}="{value}"' for key, value in (self.props or {}).items())

        # Combine everything into a valid HTML string
        if attrs:  # If there are properties
            return f'<{self.tag} {attrs}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'
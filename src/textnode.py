from enum import Enum

class TextType(Enum)
    NORMAL_TEXT = "normal"
    BOLD_TEXT = "**bold**"
    ITALIC_TEXT = "_Italic_"
    CODE_TEXT = "```Code```"
    LINKS = "urls"
    IMAGES = "images"
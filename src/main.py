from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode

def main():
    textN = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(textN)
    htmlN = HTMLNode("a", "I am a heading!", None, {"href": "https://www.bootdev.com"})
    print(htmlN)
    leafN = LeafNode("a", "I am a A ref!", {"href": "https://www.bootdev.com"})
    print(leafN)
    print(leafN.to_html())

main()
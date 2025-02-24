from textnode import TextType, TextNode
from htmlnode import HTMLNode

def main():
    textN = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(textN)
    htmlN = HTMLNode("h1", "I am a heading!", None, {"href": "https://www.bootdev.com"})
    print(htmlN)

main()
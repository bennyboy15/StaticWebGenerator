from textnode import TextType, TextNode

def main():
    textN = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(textN)

main()
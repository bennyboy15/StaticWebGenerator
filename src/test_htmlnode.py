import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):

    def test_not_eq(self):
        node = HTMLNode("h1", "I am a heading!", None, {"href": "https://www.bootdev.com"})
        node2 = HTMLNode("p", "I am a paragraph", None, {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("h1", "I am a heading!", None, {"href": "https://www.bootdev.com"})
        self.assertEqual(node.__repr__(), "HTMLNode(h1, I am a heading!, None, {'href': 'https://www.bootdev.com'})")


if __name__ == "__main__":
    unittest.main()
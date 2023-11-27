# test_trie.py
import unittest
from trie import insert_radix_tree, search_radix_tree, Trie, TrieNode

class TestTrie(unittest.TestCase):
    def test_insert_radix_tree(self):
        root = TrieNode()
        insert_radix_tree(root, "apple")
        self.assertTrue(search_radix_tree(root, "apple"))
        self.assertFalse(search_radix_tree(root, "app"))
        self.assertFalse(search_radix_tree(root, "orange"))

    def test_trie_insert_search(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertFalse(trie.search("orange"))

        trie.insert("orange")
        self.assertTrue(trie.search("orange"))
        self.assertFalse(trie.search("orang"))
        self.assertFalse(trie.search("app"))

    def test_empty_trie(self):
        trie = Trie()
        self.assertFalse(trie.search("apple"))

    def test_partial_insert_search(self):
        trie = Trie()
        trie.insert("app")
        self.assertFalse(trie.search("apple"))

    def test_case_sensitivity(self):
        trie = Trie()
        trie.insert("apple")
        self.assertFalse(trie.search("Apple"))

    def test_insert_special_chars(self):
        trie = Trie()
        trie.insert("!@#$")
        self.assertTrue(trie.search("!@#$"))

    def test_insert_numbers(self):
        trie = Trie()
        trie.insert("12345")
        self.assertTrue(trie.search("12345"))
        self.assertFalse(trie.search("123"))

if __name__ == '__main__':
    unittest.main()

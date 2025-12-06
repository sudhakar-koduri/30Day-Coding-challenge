from trie_node import *


class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    # inserting string in trie
    def insert(self, string):
        node = self.root
        for ch in string:
            if not ch in node.children :
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True
            
    def search_prefix_node(self, string)->TrieNode:
        node = self.root
        for ch in string:
            if not ch in node.children :
                return None
            node = node.children[ch]
        if node == self.root:
            return None
        return node
        
    # searching for a string
    def search(self, string):
        node = self.search_prefix_node(string)
        if node and node.is_word:
            return True
        return False
    
    # searching for a prefix
    def search_prefix(self, prefix):
        node = self.search_prefix_node(prefix)
        if node:
            return True
        return False

# Driver Code
def main():
    keys = ["the", "a", "there", "answer"]
    trie_for_keys = Trie()
    num = 1
    for x in keys:
        print(num, ".\tInsert key: '", x, "'", sep="")
        trie_for_keys.insert(x)
        num += 1
        print("-" * 100)

    search = ["a", "answer", "xyz", "an"]
    for y in search:
        print(num, ".\tSearch key: '", y, "'", sep="")
        print("\tKey found? ", trie_for_keys.search(y), sep="")
        num += 1
        print("-" * 100)

    searchPrefix = ["b", "an"]
    for z in searchPrefix:
        print(num, ".\tSearch prefix: '", z, "'", sep="")
        print("\tPrefix found? ", trie_for_keys.search_prefix(z), sep="")
        num += 1
        print("-" * 100)


if __name__ == "__main__":
    main()
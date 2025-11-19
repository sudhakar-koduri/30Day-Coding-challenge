from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(list)
        self.is_end_of_word = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        node = self.root
        for char in word[::-1]:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]  
        if node != self.root:
            node.is_end_of_word = True
    
    def getChildNode(self,character, node=None):
        if node == None:
            node = self.root
        if character in node.children:    
            return node.children[character] 
        else:
            return None

class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trieTree = Trie()
        self.queue = list()
        # map(self.trieTree.addWord, words)
        for word in words:
            self.trieTree.addWord(word)

        
    def query(self, letter)->bool:
        """
        :type letter: str
        :rtype: bool
        """
        self.queue.append(letter)
        currNode:TrieNode = None

        for character in self.queue[::-1]:
            currNode = self.trieTree.getChildNode(character, currNode)
            if currNode: 
                if currNode.is_end_of_word :
                    return True
            else:
                return False
        return False
    
checker = StreamChecker(["cat","ate"])
for ch in "dcate":
    print(ch,checker.query(ch))


from collections import deque
class StreamChecker_sol:

    def __init__(self, words):
        self.trie = {}
        self.stream = deque([])

        for word in set(words):
            node = self.trie   
            for ch in word[::-1]:
                if not ch in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = word
        
    def query(self, letter):
        self.stream.appendleft(letter)
        
        node = self.trie
        for ch in self.stream:
            if '$' in node:
                return True
            if not ch in node:
                return False
            node = node[ch]
        return '$' in node
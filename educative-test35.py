
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def get_root(self):
        return self.root


def longest_common_prefix_trie(strs):
  
    trie_ds = Trie()
    min_lt = min(len(str) for str in strs)
    for str in strs:
        trie_ds.insert(str[0:min_lt])
        
    root_node = trie_ds.get_root()
    common_prefix_lt = 0
    while root_node and not root_node.is_end_of_word and len(root_node.children.items()) == 1:
        common_prefix_lt += 1
        root_node = list(root_node.children.values())[0]
        # char, next_node = list(node.children.items())[0]
        # prefix += char
        # node = next_node
    return strs[0][:common_prefix_lt]

def longest_common_prefix(strs):
  
    common = strs[0]
    for str in strs[1:]:
        matched = -1
        for idx in range( min(len(common), len(str)) ):
            if common[idx] == str[idx]:
                matched = idx
            else:
                break
        if matched == -1:
            return ""
        else:
            common = str[0:matched+1]
    return common


test_cases = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["interspecies", "interstellar", "interstate"],
        ["throne", "dungeon"],
        ["throne", "throne"],
        ["apple", "app"],
        ["a", "b", "c"],
        ["reflower", "flow", "flight"],
        ["preach", "prevent", "prelude", "press"],
    ]
import time

start_time = time.time()
for case in test_cases:
    print(f'{case} --> {longest_common_prefix_trie(case)}')
print("time took :", time.time() - start_time )
start_time = time.time()
for case in test_cases:
    print(f'{case} --> {longest_common_prefix(case)}')
print("time took :", time.time() - start_time )

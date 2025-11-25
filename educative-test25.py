from collections import defaultdict, deque
class suffixNode:
    def __init__(self, index_pos=-1, len=0 ):
        self.children = {}
        # self.data = data
        self.index_pos = index_pos
        self.word_len = len

def stringIndices(wordsContainer, wordsQuery):
    result_idx_list = [-1] * len(wordsQuery)
    head = suffixNode()

    min_idx = 0
    min_lt = len(wordsContainer[0])
    for idx, word in enumerate(wordsContainer):
        if len(word) < min_lt:
            min_lt = len(word)
            min_idx = idx
        parent_node = head
        for ch in word[::-1]:
            curr_node = None
            if ch in parent_node.children:
                curr_node = parent_node.children[ch]
            if not curr_node:
                curr_node = suffixNode()
                parent_node.children[ch] = curr_node
            parent_node = curr_node
        if "$" not in parent_node.children:
            parent_node.children["$"] = suffixNode(idx, len(word))

    for idx, query in enumerate(wordsQuery):
        curr_node = head
        for ch in query[::-1]:
            if ch in curr_node.children:
                curr_node =  curr_node.children[ch]
            else:
                break;
        if curr_node == head:
            result_idx_list[idx] = min_idx
        else:
            result_word = len(wordsContainer)
            queue = deque([curr_node])
            child_nodes = []
            while queue:
                next_node = queue.popleft()
                if "$" in next_node.children:
                    result_word = min(result_word, next_node.children["$"].index_pos)
                else:
                    for data, child in next_node.children.items():
                        if data != "$":
                          child_nodes.append(child)
                if not queue:
                    # Processed all the current level nodes
                    if result_word == len(wordsContainer):
                        # Found no word in current level - process children in the next level
                        queue.extend(child_nodes)
                        child_nodes.clear()
            # Set the found word idx to result list
            if result_word == len(wordsContainer):
                result_word = min_idx     
            result_idx_list[idx] = result_word
    return result_idx_list

# print(stringIndices(["bat","z","tucat","cat"],["at","cat","xz"]))
# print(stringIndices(["mango","ango","xango"],["go","ango","fts"]))
# print(stringIndices(["flight","night","tight","light"],["ight", "t", "zzz"]))
# print(stringIndices(["hello","yellow","mellow","fellow"],["low","ellow","wow"]))
# print(stringIndices(["cart","start","part","art"],["art","rt","xyz"]))
# print(stringIndices(["abcde","bcde","cde"],["abcde","bcde","cde"]))
print(stringIndices(["rums","rums","rumsx","rumsy"] , ["rums","rumszz","zzrums"]))

# Save the best index value at each node instead of just the leaf node 
def stringIndices_sol(wordsContainer, wordsQuery):
    trie = {}

    # Build the reversed trie
    for index, word in enumerate(wordsContainer):
        currentNode = trie

        # Update best candidate at root
        if None not in currentNode or currentNode[None][1] > len(word):
            currentNode[None] = (index, len(word))

        for char in reversed(word):
            if char not in currentNode:
                currentNode[char] = {}
            currentNode = currentNode[char]

            # Update best candidate at this node
            if None not in currentNode or currentNode[None][1] > len(word):
                currentNode[None] = (index, len(word))

    # Query phase
    result = []
    for queryWord in wordsQuery:
        currentNode = trie
        for char in reversed(queryWord):
            if char not in currentNode:
                break
            currentNode = currentNode[char]
        result.append(currentNode[None][0])

    return result
from collections import defaultdict

def group_anagrams_sort(strs):

    sorted_word_map = defaultdict(list)
    for str in strs:
       sorted_word_map["".join(sorted(str))].append(str)    

    return list(sorted_word_map.values())

print(group_anagrams_sort(["duel","cars","deul","speed","spede","dule"]))

# Using the count method to find anagram
def group_anagrams_count(strs):
    res = {}

    for s in strs:
        count = [0] * 26
        for i in s:
            index = ord(i) - ord('a')
            count[index] += 1
    
        key = tuple(count)

        if key in res:
            res[key].append(s)
        else:
            res[key] = [s]

    return res.values()
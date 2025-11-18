# from UnionFind import UnionFind
# Helper: Decide if two strings are similar
def areSimilar(s1, s2):
    diff = []                               
    for a, b in zip(s1, s2):               
        if a != b:                       
            diff.append((a, b))
            if len(diff) > 2:        
                return False

    return (len(diff) == 0) or (
        len(diff) == 2 and diff[0] == diff[1][::-1]
    )

def numSimilarGroups(strs):
    def isSimilar(s, t):
            swaps = 0
            l, r = 0, len(s) - 1
            while l <= r:
                if (s[l] != t[l] and s[r] != t[r]):
                    if s[l] != t[r] or s[r] != t[l]: return False
                    l += 1
                    r -= 1
                    swaps += 1
                if s[l] == t[l]: l += 1
                if s[r] == t[r]: r -= 1
            return swaps <= 1
    grp_map = { str: idx for idx,str in enumerate(strs) }

    for i1, str1 in enumerate(strs):
        if grp_map[str1] != i1:
            continue
        for i2, str2 in enumerate(strs):
            if i1 == i2:
                continue;
            dist_set = set()
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                   dist_set.add(str1[i])
            dist = len(dist_set)
            # if dist == 2 or dist == 0:
            if areSimilar(str1, str2):
               minGrp = min(grp_map[str1], grp_map[str2])
               grp_map[str1] = grp_map[str2] = minGrp
               break
    return len(set(grp_map.values()))

# print(numSimilarGroups(["abcd","abdc","acbd","bdca"]))
# print(numSimilarGroups(["abc","acb","bac","bca", "cab", "cba"]))
# print(numSimilarGroups(["jhki","kijh","jkhi","kihj", "ijhk"]))
print(numSimilarGroups(
["nqqqhidshfsdldpxcrxybbeoldoyqmxiplpvbwetwuqlaqnuqcfegslkyszgoigdjaqwcga","nqqqhidshfsdldpxcrxybbeopdoyqmxipllvbwgtwuqlaqnuqcfegslkyszeoigdjaqwcga","nqqqhidshfsdldpxcrxybbeoldoyqmxiplpvbwgtwuqlaqnuqcfegslkyszeoigdjaqwcga","nqqqhidshfsdldpxcrxybbeoldoyqmxiplpvkwgtwuqlaqnuqcfegslbyszeoigdjaqwagc","nqqqhidshfsdldpxcrxybbeoldoyqmxiplpvkwgtwuqlaqnuqcfegslbyszeoigdjaqwcga","oqqqhidshfsdldpxcrxybbeoldnyqmxiplpvkwgtwuqlaqnuqcfegslbyszeoigdjaqwcga"]))


from typing import List
# from UnionFind import UnionFind 



# def numSimilarGroups_sol(strs):
#     n = len(strs)
#     uf = UnionFind(n)                  

#     for i in range(n):
#         for j in range(i + 1, n):
#             if areSimilar(strs[i], strs[j]):
#                 uf.union(i, j)           

#     roots = {uf.find(i) for i in range(n)}  
#     return len(roots)
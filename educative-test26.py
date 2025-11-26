def is_anagram(str1, str2):

    if len(str1) == len(str2):
        return ''.join(sorted(str1)) == ''.join(sorted(str2))
    return False

# Using the hash table approach
def is_anagram_sol(str1, str2):
    if len(str1) != len(str2):
        return False
    
    table = {}
    
    for i in str1:
      if i in table:
        table[i] += 1
      
      else:
        table[i] = 1
    
    for i in str2:
      if i in table:
        table[i] -= 1
      
      else:
        return False
    
    for key in table:
        if table[key] != 0:
            return False
    
    return True
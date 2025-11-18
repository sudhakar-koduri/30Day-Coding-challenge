from collections import defaultdict

def max_substring_length(s):
    char_map = defaultdict(list)
    char_list = []
    for idx, c in enumerate(s):
        if c in char_map:
            pos_arr = char_map[c]
            pos_arr[1] = idx
        else:
            char_map[c] = [idx, idx]
            char_list.append(c)
    # next_pos = min(1, len(char_list)-1)
    full_sets = []
    invalid_charset = []
    skip_chars = set()
    for curr_char in char_list:
        if curr_char in skip_chars:
            continue
        st_pos = char_map[curr_char][0]
        end_pos = char_map[curr_char][1]
        
        # scan the range of all characters enclosed by the currChar
        end_pos2 = -1
        st_pos2 = len(s)      
        cset_currchar_range = set(s[st_pos:end_pos+1])
        for ch2 in cset_currchar_range:
            if ch2 in invalid_charset:
                # Range got invalid one
                invalid_charset.append(curr_char)
                break
            end_pos2 = max(end_pos2, char_map[ch2][1])
            st_pos2 = min(st_pos2, char_map[ch2][0])

        if curr_char in invalid_charset:
            continue

        # length constraint
        if (end_pos2 - st_pos2+1) == len(s):
            invalid_charset.append(curr_char)
            continue

        # full-set check
        isFullSet = len(cset_currchar_range) == len(set(s[st_pos2:end_pos2+1]))
        if isFullSet:
            full_sets.append([st_pos2, end_pos2])
            skip_chars.update(cset_currchar_range)
        else:
            invalid_charset.append(curr_char)
            continue

    max_lt = -1
    curr_idx = 0
    while curr_idx < len(full_sets):
        st_pos, end_pos = full_sets[curr_idx][0], full_sets[curr_idx][1]
        curr_max = end_pos - st_pos + 1
        prev_end = end_pos
        
        # Merge next intervals
        for st_pos2, end_pos2 in full_sets[curr_idx+1:]:
            if st_pos2 == prev_end+1 :
                curr_idx += 1
                if end_pos2-st_pos+1 == len(s) :
                   if end_pos2 - st_pos2 > end_pos - st_pos:
                       curr_max += end_pos2 - st_pos2 - (end_pos - st_pos)    
                else:
                    curr_max += end_pos2 - st_pos2 + 1
                prev_end = end_pos2

        max_lt = max(max_lt, curr_max)
        curr_idx += 1
    return max_lt

print(max_substring_length("abacd"))
print(max_substring_length("xyxy"))
print(max_substring_length("aa"))
print(max_substring_length("xyyxzaa"))

def max_substring_length_sol(s):
    first = {}
    last = {}
    for i, c in enumerate(s):
        if c not in first:
            first[c] = i
        last[c] = i

    max_len = -1
    
    for c1 in first:
        start = first[c1]
        end = last[c1]
        j = start
        
        while j < len(s):
            c2 = s[j]
            if first[c2] < start:
                break
            end = max(end, last[c2])
            if end == j and end - start + 1 != len(s):
                max_len = max(max_len, end - start + 1)
            j += 1

    return max_len
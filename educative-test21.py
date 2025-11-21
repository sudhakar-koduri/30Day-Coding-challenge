def isPrefixOfWord(sentence, searchWord):
    match_idx = -1
    curr_idx = 0
    search_len = len(searchWord)
    for curr_idx, word in enumerate(sentence.split()):
        match_pos = 0
        # isMatched = true
        for pos in range(search_len):            
            if word[pos] != searchWord[pos]:
                break;
            match_pos += 1
        if match_pos == search_len:
            match_idx = curr_idx+1
            break;
    # Replace this placeholder return statement with your code
    return match_idx

print(isPrefixOfWord("i love coding" , "lov"))
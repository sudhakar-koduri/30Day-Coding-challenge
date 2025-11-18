
def kEmptySlots(bulbs, k):
    arr = [False] * (len(bulbs)+1)
    day = 0
    for day, pos in enumerate(bulbs, start=1):
        arr[pos] = True
        if day == 1:
            continue 
        # check left for sol
        if pos > 1 and pos-k-1 >= 1:
            peerPos = pos-k
            valid = True
            if (k != 0):
                for trail in range(peerPos,pos):
                    if (arr[trail]):
                        valid = False
                        break
            if valid and arr[peerPos-1]:
                return day
        # check right for sol
        if pos < len(bulbs) and pos+k+1 <= len(bulbs):
            peerPos = pos+k
            valid = True
            if (k != 0):
                for trail in range(pos+1, peerPos+1):
                    if (arr[trail]):
                        valid = False
                        break
            if valid and arr[peerPos+1]:
                return day
    return -1

print (kEmptySlots([2,4,1,3], 0))
def lucky_numbers(matrix):
    
    rows = len(matrix)
    cols = len(matrix[0])
    row_min_set = set()
    for r in range(rows):
        min_val = matrix[r][0]
        for c in range(cols):
            min_val = min(min_val, matrix[r][c])
        row_min_set.add(min_val)
    for c in range(cols):
        max_val= max(matrix[r][c] for r in range(rows))
        if max_val in row_min_set:
            return [max_val]
    return []

print(lucky_numbers([[3,7,8],[9,11,13],[15,16,17]]))

print(lucky_numbers( [[10,20,30,40],[5,25,35,50],[60,70,80,90],[100,110,120,130]] ))
print(lucky_numbers( [[12,18,23,50],[5,16,25,45],[4,15,26,48],[3,14,27,60]] ))
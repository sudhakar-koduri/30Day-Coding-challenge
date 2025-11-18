def set_matrix_zeros(mat):
    row_cnt = len(mat)
    col_cnt = len(mat[0])
    rows = [1]*row_cnt
    cols = [1]*col_cnt
    for row in range(0,row_cnt):
      for col in range(0,col_cnt):
        if mat[row][col] == 0:
          cols[col] = 0
          rows[row] = 0

    for row3, val in enumerate(rows):
      if val == 0:
        for col2 in range(0,col_cnt):
            mat[row3][col2] = 0
    for col3, val in enumerate(cols):
      if val == 0:
        for row2 in range(0,row_cnt):
            mat[row2][col3] = 0
            
    return mat

print(set_matrix_zeros([[2,6,5,4,9,1],[7,2,0,0,5,4],[1,1,1,1,0,1],[9,8,2,0,1,3],[7,8,6,5,4,3],[9,8,1,2,5,6]]))
#    [[257,396,754,665,697,229,381,0,788,604,25,636,20,587,951,56,935,593,98,993],[636,985,720,595,577,688,504,668,656,477,994,373,902,77,752,329,273,164,268,589],[846,810,647,623,0,53,892,281,414,699,448,834,243,703,461,0,522,20,118,723],[676,477,149,362,530,691,481,138,989,80,457,651,589,47,832,755,142,356,896,0],[598,335,204,259,156,83,323,918,138,893,642,282,0,634,928,186,362,726,609,825],[0,0,505,363,408,290,312,3,985,949,422,457,959,30,542,897,403,55,76,328],[557,943,439,673,49,10,512,533,233,152,848,662,882,810,935,603,0,229,402,555],[449,312,732,866,671,589,687,132,249,647,635,744,802,0,546,439,122,829,110,954],[726,437,409,976,53,559,1,857,0,613,675,381,108,234,179,274,637,221,398,554],[0,240,270,379,801,465,0,175,895,745,526,353,309,26,504,995,76,705,765,773],[721,981,263,957,319,553,459,693,853,948,451,964,549,69,100,189,682,287,842,8],[749,875,564,497,701,205,960,99,663,159,570,49,450,747,718,913,425,436,532,368],[917,556,862,594,886,854,115,524,308,818,753,483,802,420,7,876,636,575,345,985],[871,955,159,242,993,930,899,559,57,694,777,204,575,653,173,4,846,347,717,91],[426,499,28,786,909,377,727,139,0,270,448,415,816,741,831,800,735,662,894,400]]))
    # [0, 0, 720, 595, 0, 688, 0, 0, 0, 477, 994, 373, 0, 0, 752, 0, 0, 164, 268, 0]
    # [0, 0, 720, 595, 0, 688, 504, 0, 0, 477, 994, 373, 0, 0, 752, 0, 0, 164, 268, 0]

# Matrix pattern: key idea behind this algorithm is to use the matrix’s first row and column as storage space to track which rows and columns need to be zeroed, thus eliminating the need for additional data structures. The corresponding positions in the first row and column are marked when a zero is found. These markers then set the entire row or column to zero in a second pass through the matrix. Using this approach, the algorithm modifies the matrix with minimal extra space required.
def set_matrix_zeros_sol(mat):
	rows = len(mat)
	cols = len(mat[0])
	fcol = False
	frow = False

	for i in range(rows):
		if mat[i][0] == 0:
			fcol = True

	for i in range(cols):
		if mat[0][i] == 0:
			frow = True

	for i in range(1, rows):
		for j in range(1, cols):
			if mat[i][j] == 0:
				mat[0][j] = mat[i][0] = 0

	for i in range(1, rows):
		if mat[i][0] == 0:
			for j in range(1, cols):
				mat[i][j] = 0

	for j in range(1, cols):
		if mat[0][j] == 0:
			for i in range(1, rows):
				mat[i][j] = 0

	if fcol:
		for i in range(rows):
			mat[i][0] = 0

	if frow:
		for j in range(cols):
			mat[0][j] = 0
	return mat
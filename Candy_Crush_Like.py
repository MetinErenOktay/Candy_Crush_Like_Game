import sys
with open(sys.argv[1], "r+") as f:
    #creates a list of row list that contains context of the input file
    l_of_l_by_row = []
    for line in f:
        stripped_line = line.strip()  # slices content of txt file line by line
        line_list = stripped_line.split(' ')  # slices content of the line by tab spaces
        l_of_l_by_row.append(line_list)
for row in l_of_l_by_row:
    print('  '.join(str(x) for x in row))

score=0
print("\nYour score is:", score)
previous_removed_count=0


while True:

    # this part finishes the loop that gets inputs if there is no neighbor with ball of the same color and also there is no bomb (x) in a cell
    state_X = 0
    possible_matching = [[] for _ in range(len(l_of_l_by_row))]
    for poss in range(len(l_of_l_by_row)):
        for matc in range(len(l_of_l_by_row[0])):
            if len(l_of_l_by_row) != 1 and len(l_of_l_by_row[0]) != 1 and poss == 0 and matc == 0:
                # adds admatc acent elements without the same value to the list of list possible_matching
                if l_of_l_by_row[poss][matc] != l_of_l_by_row[poss + 1][matc] and l_of_l_by_row[poss][matc] != l_of_l_by_row[poss][matc + 1]:
                    possible_matching[poss].append(l_of_l_by_row[poss][matc])
                else:
                    possible_matching[poss].append(" ")
            elif len(l_of_l_by_row) != 1 and len(l_of_l_by_row[0]) != 1 and poss == 0 and matc == len(l_of_l_by_row[poss]) - 1:
                if l_of_l_by_row[poss][matc] != l_of_l_by_row[poss + 1][matc] and l_of_l_by_row[poss][matc - 1] != l_of_l_by_row[poss][matc]:
                    possible_matching[poss].append(l_of_l_by_row[poss][matc])
                else:
                    possible_matching[poss].append(" ")
            elif len(l_of_l_by_row) != 1 and len(l_of_l_by_row[0]) != 1 and poss == 0 and matc > 0 and matc < len(l_of_l_by_row[poss]) - 1:
                if l_of_l_by_row[poss][matc] != l_of_l_by_row[poss + 1][matc] and l_of_l_by_row[poss][matc] != l_of_l_by_row[poss][matc + 1] and l_of_l_by_row[poss][matc - 1] != l_of_l_by_row[poss][matc]:
                    possible_matching[poss].append(l_of_l_by_row[poss][matc])
                else:
                    possible_matching[poss].append(" ")
            elif len(l_of_l_by_row) != 1 and len(l_of_l_by_row[0]) != 1 and poss == len(l_of_l_by_row) - 1 and matc == 0:
                if l_of_l_by_row[poss - 1][matc] != l_of_l_by_row[poss][matc] and l_of_l_by_row[poss][matc] != l_of_l_by_row[poss][matc + 1]:
                    possible_matching[poss].append(l_of_l_by_row[poss][matc])
                else:
                    possible_matching[poss].append(" ")
            elif len(l_of_l_by_row) != 1 and len(l_of_l_by_row[0]) != 1 and poss == len(l_of_l_by_row) - 1 and matc == len(l_of_l_by_row[poss]) - 1:
                if l_of_l_by_row[poss - 1][matc] != l_of_l_by_row[poss][matc] and l_of_l_by_row[poss][matc - 1] != l_of_l_by_row[poss][matc]:
                    possible_matching[poss].append(l_of_l_by_row[poss][matc])
                else:
                    possible_matching[poss].append(" ")
            elif len(l_of_l_by_row) != 1 and len(l_of_l_by_row[0]) != 1 and poss == len(l_of_l_by_row) - 1 and matc > 0 and matc < len(l_of_l_by_row[poss]) - 1:
                if l_of_l_by_row[poss - 1][matc] != l_of_l_by_row[poss][matc] and l_of_l_by_row[poss][matc] != l_of_l_by_row[poss][matc + 1] and l_of_l_by_row[poss][matc - 1] != l_of_l_by_row[poss][matc]:
                    possible_matching[poss].append(l_of_l_by_row[poss][matc])
                else:
                    possible_matching[poss].append(" ")
            elif len(l_of_l_by_row) != 1 and len(l_of_l_by_row[0]) != 1 and poss > 0 and poss < len(l_of_l_by_row) - 1 and matc == 0:
                if l_of_l_by_row[poss][matc] != l_of_l_by_row[poss + 1][matc] and l_of_l_by_row[poss - 1][matc] != l_of_l_by_row[poss][matc] and l_of_l_by_row[poss][matc] != l_of_l_by_row[poss][matc + 1]:
                    possible_matching[poss].append(l_of_l_by_row[poss][matc])
                else:
                    possible_matching[poss].append(" ")
            elif len(l_of_l_by_row) != 1 and len(l_of_l_by_row[0]) != 1 and poss > 0 and poss < len(l_of_l_by_row) - 1 and matc == len(l_of_l_by_row[poss]) - 1:
                if l_of_l_by_row[poss][matc] != l_of_l_by_row[poss + 1][matc] and l_of_l_by_row[poss - 1][matc] != l_of_l_by_row[poss][matc] and l_of_l_by_row[poss][matc - 1] != l_of_l_by_row[poss][matc]:
                    possible_matching[poss].append(l_of_l_by_row[poss][matc])
                else:
                    possible_matching[poss].append(" ")
            elif len(l_of_l_by_row) != 1 and len(l_of_l_by_row[0]) != 1 and poss > 0 and poss < len(l_of_l_by_row) - 1 and matc > 0 and matc < len(l_of_l_by_row[poss]) - 1:
                if l_of_l_by_row[poss][matc] != l_of_l_by_row[poss + 1][matc] and l_of_l_by_row[poss - 1][matc] != l_of_l_by_row[poss][matc] and l_of_l_by_row[poss][matc] != l_of_l_by_row[poss][matc + 1] and l_of_l_by_row[poss][matc - 1] != l_of_l_by_row[poss][matc]:
                    possible_matching[poss].append(l_of_l_by_row[poss][matc])
                else:
                    possible_matching[poss].append(" ")
            elif len(l_of_l_by_row) == 1 and len(l_of_l_by_row[0]) == 1:
                possible_matching[poss].append(l_of_l_by_row[poss][matc])

            elif len(l_of_l_by_row) == 1 and len(l_of_l_by_row[0]) != 1 and matc == 0:
                if l_of_l_by_row[poss][matc] != l_of_l_by_row[poss][matc + 1]:
                    possible_matching[poss].append(l_of_l_by_row[poss][matc])
                else:
                    possible_matching[poss].append(" ")
            elif len(l_of_l_by_row) == 1 and len(l_of_l_by_row[0]) != 1 and matc == len(l_of_l_by_row[poss]) - 1:
                if l_of_l_by_row[poss][matc - 1] != l_of_l_by_row[poss][matc]:
                    possible_matching[poss].append(l_of_l_by_row[poss][matc])
                else:
                    possible_matching[poss].append(" ")
            elif len(l_of_l_by_row) == 1 and len(l_of_l_by_row[0]) != 1 and matc > 0 and matc < len(l_of_l_by_row[poss]) - 1:
                if l_of_l_by_row[poss][matc] != l_of_l_by_row[poss][matc + 1] and l_of_l_by_row[poss][matc - 1] != l_of_l_by_row[poss][matc]:
                    possible_matching[poss].append(l_of_l_by_row[poss][matc])
                else:
                    possible_matching[poss].append(" ")

            elif len(l_of_l_by_row) != 1 and len(l_of_l_by_row[0]) == 1 and poss == 0:
                if l_of_l_by_row[poss][matc] != l_of_l_by_row[poss+1][matc]:
                    possible_matching[poss].append(l_of_l_by_row[poss][matc])
                else:
                    possible_matching[poss].append(" ")
            elif len(l_of_l_by_row) != 1 and len(l_of_l_by_row[0]) == 1 and poss == len(l_of_l_by_row[poss]) - 1:
                if l_of_l_by_row[poss-1][matc] != l_of_l_by_row[poss][matc]:
                    possible_matching[poss].append(l_of_l_by_row[poss][matc])
                else:
                    possible_matching[poss].append(" ")
            elif len(l_of_l_by_row) != 1 and len(l_of_l_by_row[0]) == 1 and poss > 0 and matc < len(
                    l_of_l_by_row[poss]) - 1:
                if l_of_l_by_row[poss][matc] != l_of_l_by_row[poss+1][matc] and l_of_l_by_row[poss-1][matc] != l_of_l_by_row[poss][matc]:
                    possible_matching[poss].append(l_of_l_by_row[poss][matc])
                else:
                    possible_matching[poss].append(" ")
            if 'X' in l_of_l_by_row[poss]:
                state_X = 1
                break
    if l_of_l_by_row == possible_matching and state_X == 0:
        break

    rrooww, ccoolluummnn = input("\nPlease enter a row and column number: ").split()

    deleted_row_counter=0
    for delete in range(len(l_of_l_by_row)):
        for emp in range(len(l_of_l_by_row[0])):
            if (l_of_l_by_row[delete-deleted_row_counter].count(' ') == len(l_of_l_by_row[delete-deleted_row_counter])):
                del l_of_l_by_row[delete]
                deleted_row_counter += 1

    try:
        a=l_of_l_by_row[int(rrooww)][int(ccoolluummnn)]
        copy_of_l_of_l_by_row=l_of_l_by_row.copy()
        if len(l_of_l_by_row) - 1 < int(rrooww) or len(l_of_l_by_row[0]) - 1 < int(ccoolluummnn) or a == " ":
            raise IndexError
        if l_of_l_by_row[int(rrooww)][int(ccoolluummnn)] == 'X':
            x_count = 0
            deleted_sublist_counter = 0
            extra_bomb_lst = [[int(rrooww), int(ccoolluummnn)]]
            for m in range(len(copy_of_l_of_l_by_row)):
                for n in range(len(copy_of_l_of_l_by_row[m])):
                    if (m == int(rrooww) or n == int(ccoolluummnn)) and copy_of_l_of_l_by_row[m][n] == "X" and [m,n] != [int(rrooww), int(ccoolluummnn)] and [m, n] not in extra_bomb_lst:
                        extra_bomb_lst.append([m, n])
                    if copy_of_l_of_l_by_row[int(rrooww)].count("X") > 1 or copy_of_l_of_l_by_row[m][
                        int(ccoolluummnn)].count("X") > 1:
                        x_count += 1
            # this part calculates the score
            row_lst_of_scoring_of_X = list({sub[0] for sub in extra_bomb_lst})
            column_lst_of_scoring_of_X = list({sub[1] for sub in extra_bomb_lst})
            for h in range(len(row_lst_of_scoring_of_X)):
                for u in range(len(l_of_l_by_row[h])):
                    if l_of_l_by_row[row_lst_of_scoring_of_X[h]][u] == "B":
                        score_increment = 9
                    elif l_of_l_by_row[row_lst_of_scoring_of_X[h]][u] == "G":
                        score_increment = 8
                    elif l_of_l_by_row[row_lst_of_scoring_of_X[h]][u] == "W":
                        score_increment = 7
                    elif l_of_l_by_row[row_lst_of_scoring_of_X[h]][u] == "Y":
                        score_increment = 6
                    elif l_of_l_by_row[row_lst_of_scoring_of_X[h]][u] == "R":
                        score_increment = 5
                    elif l_of_l_by_row[row_lst_of_scoring_of_X[h]][u] == "P":
                        score_increment = 4
                    elif l_of_l_by_row[row_lst_of_scoring_of_X[h]][u] == "O":
                        score_increment = 3
                    elif l_of_l_by_row[row_lst_of_scoring_of_X[h]][u] == "D":
                        score_increment = 2
                    elif l_of_l_by_row[row_lst_of_scoring_of_X[h]][u] == "F":
                        score_increment = 1
                    elif l_of_l_by_row[row_lst_of_scoring_of_X[h]][u] == "X":
                        score_increment = 0
                    score += score_increment
                    score_increment = 0
            for g in range(len(column_lst_of_scoring_of_X)):
                for v in range(len(l_of_l_by_row)):
                    if l_of_l_by_row[v][column_lst_of_scoring_of_X[g]] == "B":
                        score_increment = 9
                    elif l_of_l_by_row[v][column_lst_of_scoring_of_X[g]] == "G":
                        score_increment = 8
                    elif l_of_l_by_row[v][column_lst_of_scoring_of_X[g]] == "W":
                        score_increment = 7
                    elif l_of_l_by_row[v][column_lst_of_scoring_of_X[g]] == "Y":
                        score_increment = 6
                    elif l_of_l_by_row[v][column_lst_of_scoring_of_X[g]] == "R":
                        score_increment = 5
                    elif l_of_l_by_row[v][column_lst_of_scoring_of_X[g]] == "P":
                        score_increment = 4
                    elif l_of_l_by_row[v][column_lst_of_scoring_of_X[g]] == "O":
                        score_increment = 3
                    elif l_of_l_by_row[v][column_lst_of_scoring_of_X[g]] == "D":
                        score_increment = 2
                    elif l_of_l_by_row[v][column_lst_of_scoring_of_X[g]] == "F":
                        score_increment = 1
                    elif l_of_l_by_row[v][column_lst_of_scoring_of_X[g]] == "X":
                        score_increment = 0
                    score += score_increment
                    score_increment = 0
            # this part shapes the new matrix
            lst_of_X = [[] for _ in range(len(copy_of_l_of_l_by_row))]
            a_of_X = copy_of_l_of_l_by_row[int(rrooww)][int(ccoolluummnn)]
            if copy_of_l_of_l_by_row[int(rrooww)][int(ccoolluummnn)] == 'X':
                # this part deletes column and row of "X"
                l = len(extra_bomb_lst)
                for a_of_X in range(0, l):
                    for b_of_X in range(0, l - a_of_X - 1):
                        if (extra_bomb_lst[b_of_X][1] > extra_bomb_lst[b_of_X + 1][1]):
                            sss = extra_bomb_lst[b_of_X]
                            extra_bomb_lst[b_of_X] = extra_bomb_lst[b_of_X + 1]
                            extra_bomb_lst[b_of_X + 1] = sss
                extra_bomb_lst.reverse()
                for index in range(len(extra_bomb_lst)):
                    i_y = extra_bomb_lst[index][1]
                    for TTTT in sorted(range(len(copy_of_l_of_l_by_row)), reverse=True):
                        del copy_of_l_of_l_by_row[TTTT][i_y]
                for i_x in sorted(range(len(extra_bomb_lst)), reverse=True):
                    del_row_of_func_X = extra_bomb_lst[i_x][0]
                    del copy_of_l_of_l_by_row[del_row_of_func_X]
                    break

                for i_l_x in range(len(copy_of_l_of_l_by_row)):
                    for j_l_x in range(len(copy_of_l_of_l_by_row[i_l_x])):
                        lst_of_X[i_l_x].append(copy_of_l_of_l_by_row[i_l_x][j_l_x])
                for i_l_x in range(len(lst_of_X)):
                    if lst_of_X[i_l_x - deleted_sublist_counter] == []:
                        del lst_of_X[i_l_x]
            res=lst_of_X
        else:
            # this part shapes the new matrix
            consecutive_lst = []
            #stores indexes of the consecutive cells whose values are equal to the value of input cell into a list
            def censecutivity(roww, columnn):
                roww = int(roww)
                columnn = int(columnn)
                if roww >= 1:
                    if l_of_l_by_row[roww - 1][columnn] == a and l_of_l_by_row[roww][columnn] == \
                            l_of_l_by_row[roww - 1][columnn] and [roww - 1, columnn] not in consecutive_lst:
                        consecutive_lst.append([roww - 1, columnn])
                if columnn >= 1:
                    if l_of_l_by_row[roww][columnn - 1] == a and l_of_l_by_row[roww][columnn] == l_of_l_by_row[roww][columnn - 1] and [roww, columnn - 1] not in consecutive_lst:
                        consecutive_lst.append([roww, columnn - 1])
                if roww <= len(l_of_l_by_row) - 2:
                    if l_of_l_by_row[roww + 1][columnn] == a and l_of_l_by_row[roww][columnn] == \
                            l_of_l_by_row[roww + 1][columnn] and [roww + 1, columnn] not in consecutive_lst:
                        consecutive_lst.append([roww + 1, columnn])
                if columnn <= len(l_of_l_by_row[0]) - 2:
                    if l_of_l_by_row[roww][columnn + 1] == a and l_of_l_by_row[roww][columnn] == l_of_l_by_row[roww][columnn] and [roww, columnn + 1] not in consecutive_lst:
                        consecutive_lst.append([roww, columnn + 1])
            censecutivity(rrooww, ccoolluummnn)
            for el0, el1 in consecutive_lst:
                censecutivity(el0, el1)
            res = [[] for _ in range(len(l_of_l_by_row))]
            #to avoid IndexError, I divided range of value to 3(those are min limit, max limit and between them).Since we have 3 subrange for i and 3 subrange for j, we have 9 combinations of them.
            for i in range(len(l_of_l_by_row)):
                for j in range(len(l_of_l_by_row[i])):
                    if i == 0 and j == 0:
                        #adds adjacent elements without the same value to the list of list res
                        if l_of_l_by_row[i][j] != l_of_l_by_row[i + 1][j] and l_of_l_by_row[i][j] != l_of_l_by_row[i][j + 1]:
                            res[i].append(l_of_l_by_row[i][j])
                        #adds adjacent elements with the same value other than the current output to the list of list res(if this part doesn't exist, all adjacent elements with the same value will deleted in just one turn)
                        elif l_of_l_by_row[i][j] == a and [i, j] not in consecutive_lst:
                            res[i].append(l_of_l_by_row[i][j])
                        elif l_of_l_by_row[i][j] != a:
                            res[i].append(l_of_l_by_row[i][j])
                        else:
                            res[i].append(" ")
                    elif i == 0 and j == len(l_of_l_by_row[i]) - 1:
                        if l_of_l_by_row[i][j] != l_of_l_by_row[i + 1][j] and l_of_l_by_row[i][j - 1] != l_of_l_by_row[i][j]:
                            res[i].append(l_of_l_by_row[i][j])
                        elif l_of_l_by_row[i][j] == a and [i, j] not in consecutive_lst:
                            res[i].append(l_of_l_by_row[i][j])
                        elif l_of_l_by_row[i][j] != a:
                            res[i].append(l_of_l_by_row[i][j])
                        else:
                            res[i].append(" ")
                    elif i == 0 and j > 0 and j < len(l_of_l_by_row[i]) - 1:
                        if l_of_l_by_row[i][j] != l_of_l_by_row[i + 1][j] and l_of_l_by_row[i][j] != l_of_l_by_row[i][j + 1] and l_of_l_by_row[i][j - 1] != l_of_l_by_row[i][j]:
                            res[i].append(l_of_l_by_row[i][j])
                        elif l_of_l_by_row[i][j] == a and [i, j] not in consecutive_lst:
                            res[i].append(l_of_l_by_row[i][j])
                        elif l_of_l_by_row[i][j] != a:
                            res[i].append(l_of_l_by_row[i][j])
                        else:
                            res[i].append(" ")
                    elif i == len(l_of_l_by_row) - 1 and j == 0:
                        if l_of_l_by_row[i - 1][j] != l_of_l_by_row[i][j] and l_of_l_by_row[i][j] != l_of_l_by_row[i][j + 1]:
                            res[i].append(l_of_l_by_row[i][j])
                        elif l_of_l_by_row[i][j] == a and [i, j] not in consecutive_lst:
                            res[i].append(l_of_l_by_row[i][j])
                        elif l_of_l_by_row[i][j] != a:
                            res[i].append(l_of_l_by_row[i][j])
                        else:
                            res[i].append(" ")
                    elif i == len(l_of_l_by_row) - 1 and j == len(l_of_l_by_row[i]) - 1:
                        if l_of_l_by_row[i - 1][j] != l_of_l_by_row[i][j] and l_of_l_by_row[i][j - 1] != l_of_l_by_row[i][j]:
                            res[i].append(l_of_l_by_row[i][j])
                        elif l_of_l_by_row[i][j] == a and [i, j] not in consecutive_lst:
                            res[i].append(l_of_l_by_row[i][j])
                        elif l_of_l_by_row[i][j] != a:
                            res[i].append(l_of_l_by_row[i][j])
                        else:
                            res[i].append(" ")
                    elif i == len(l_of_l_by_row) - 1 and j > 0 and j < len(l_of_l_by_row[i]) - 1:
                        if l_of_l_by_row[i - 1][j] != l_of_l_by_row[i][j] and l_of_l_by_row[i][j] != l_of_l_by_row[i][j + 1] and l_of_l_by_row[i][j - 1] != l_of_l_by_row[i][j]:
                            res[i].append(l_of_l_by_row[i][j])
                        elif l_of_l_by_row[i][j] == a and [i, j] not in consecutive_lst:
                            res[i].append(l_of_l_by_row[i][j])
                        elif l_of_l_by_row[i][j] != a:
                            res[i].append(l_of_l_by_row[i][j])
                        else:
                            res[i].append(" ")
                    elif i > 0 and i < len(l_of_l_by_row) - 1 and j == 0:
                        if l_of_l_by_row[i][j] != l_of_l_by_row[i + 1][j] and l_of_l_by_row[i - 1][j] != l_of_l_by_row[i][j] and l_of_l_by_row[i][j] != l_of_l_by_row[i][j + 1]:
                            res[i].append(l_of_l_by_row[i][j])
                        elif l_of_l_by_row[i][j] == a and [i, j] not in consecutive_lst:
                            res[i].append(l_of_l_by_row[i][j])
                        elif l_of_l_by_row[i][j] != a:
                            res[i].append(l_of_l_by_row[i][j])
                        else:
                            res[i].append(" ")
                    elif i > 0 and i < len(l_of_l_by_row) - 1 and j == len(l_of_l_by_row[i]) - 1:
                        if l_of_l_by_row[i][j] != l_of_l_by_row[i + 1][j] and l_of_l_by_row[i - 1][j] != l_of_l_by_row[i][j] and l_of_l_by_row[i][j - 1] != l_of_l_by_row[i][j]:
                            res[i].append(l_of_l_by_row[i][j])
                        elif l_of_l_by_row[i][j] == a and [i, j] not in consecutive_lst:
                            res[i].append(l_of_l_by_row[i][j])
                        elif l_of_l_by_row[i][j] != a:
                            res[i].append(l_of_l_by_row[i][j])
                        else:
                            res[i].append(" ")
                    elif i > 0 and i < len(l_of_l_by_row) - 1 and j > 0 and j < len(l_of_l_by_row[i]) - 1:
                        if l_of_l_by_row[i][j] != l_of_l_by_row[i + 1][j] and l_of_l_by_row[i - 1][j] != l_of_l_by_row[i][j] and l_of_l_by_row[i][j] != l_of_l_by_row[i][j + 1] and l_of_l_by_row[i][j - 1] != l_of_l_by_row[i][j]:
                            res[i].append(l_of_l_by_row[i][j])
                        elif l_of_l_by_row[i][j] == a and [i, j] not in consecutive_lst:
                            res[i].append(l_of_l_by_row[i][j])
                        elif l_of_l_by_row[i][j] != a:
                            res[i].append(l_of_l_by_row[i][j])
                        else:
                            res[i].append(" ")
            #this part calculates the score
            deleted_element_counter = 0
            previous_deleted_element_counter=0
            for i_of_scoring_of_nonX in range(len(l_of_l_by_row)):
                for j_of_scoring_of_nonX in range(len(l_of_l_by_row[i_of_scoring_of_nonX])):
                    if l_of_l_by_row[i_of_scoring_of_nonX][j_of_scoring_of_nonX] != res[i_of_scoring_of_nonX][j_of_scoring_of_nonX]:
                        deleted_element_counter += 1
            deleted_element_counter -= previous_deleted_element_counter
            if a=="B":
                score_increment=deleted_element_counter*9
            elif a=="G":
                score_increment=deleted_element_counter*8
            elif a=="W":
                score_increment=deleted_element_counter*7
            elif a=="Y":
                score_increment=deleted_element_counter*6
            elif a=="R":
                score_increment=deleted_element_counter*5
            elif a=="P":
                score_increment=deleted_element_counter*4
            elif a=="O":
                score_increment=deleted_element_counter*3
            elif a=="D":
                score_increment=deleted_element_counter*2
            elif a=="F":
                score_increment=deleted_element_counter*1
            score+=score_increment
            previous_deleted_element_counter += deleted_element_counter
            deleted_element_counter = 0
            score_increment = 0
        #this part slides down the element in a column if the space below is empty
        for x in range(len(res)):
            for i in range(len(res)):
                for j in range(len(res[i])):
                    if i!=0:
                        if res[i][j]==" ":
                            res[i][j]=res[i-1][j]
                            res[i-1][j]=" "
        l_of_l_by_row = res
        #for column shifting: this part creates a list of lists whose sublists represent columns from a list of lists whose sublists represent rows.
        l_of_l_by_column = []
        for j in range(len(res[0])):
            row = []
            for i in range(len(res)):
                row.append(res[i][j])
            l_of_l_by_column.append(row)
        #for column shifting: this part removes all elements of a sublist if all elements of the sublist is " ".
        res2 = [[] for _ in range(len(l_of_l_by_column))]
        for a in range(len(l_of_l_by_column)):
            for b in range(len(l_of_l_by_column[a])):
                if (l_of_l_by_column[a].count(' ') != len(l_of_l_by_column[a])):
                    res2[a].append(l_of_l_by_column[a][b])
        #for column shifting: this part removes empty lists form the list of list.
        res3=[q for q in res2 if q]
        #for column shifting: this part creates a list of lists whose sublists represent rows from a list of lists whose sublists represent columns.
        #for column shifting: our base list of lists is a list of lists whose sublists represent rows, again.
        l_of_l_by_row_again = []
        for l in range(len(res3[0])):
            column = []
            for k in range(len(res3)):
                column.append(res3[k][l])
            l_of_l_by_row_again.append(column)
        l_of_l_by_row = l_of_l_by_row_again
        #this part deletes empty rows
        for c in sorted(range(len(l_of_l_by_row)), reverse=True):
            for d in sorted(range(len(l_of_l_by_row[c])), reverse=True):
                if (l_of_l_by_row[c].count(' ') == len(l_of_l_by_row[c])):
                    del l_of_l_by_row[c]
        print(" ")
        for row in l_of_l_by_row:
            print('  '.join(str(x) for x in row))

        print("\nYour score is:", score)
    except IndexError:
        print("\nPlease enter a valid size!")
print("\nGame over!\n")

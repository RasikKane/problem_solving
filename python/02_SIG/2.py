# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(B):
    # write your code in Python 3.6
    # find dim for board
    PLAYER = 'O'
    FOW = 'X'
    try:
        N = len(B[0])
    except:  # error in input
        return 0

    # find location of "O"
    board = [list(row) for row in B]
    indices = [[i, row.index(PLAYER)] for i, row in enumerate(board) if PLAYER in row]
    # indices = [[i, row.index(PLAYER)] for i, row in enumerate(B) if PLAYER in row]

    kill_list = []

    for r,i in reversed(indices):
        row = r
        ind = i
        kills = 0
        while row > 1:
            # left kill
            flag = False
            if ind>=2 and board[row-1][ind-1] == FOW and board[row-2][ind-2] == '.':
                kills+=1
                row-=2
                ind-=2
                flag = True

            # right kill
            if N-ind>=2 and board[row-1][ind+1] == FOW and board[row-2][ind+2] == '.':
                kills += 1
                row -= 2
                ind += 2
                flag = True
            if not flag:
                row-=1

        kill_list.append(kills)

        # row = r
        # ind = i
        # kills = 0
        # while row > 1 and ((N - ind) >= 2 and (ind - 2) > 0):
        #     # right kill
        #     if N-ind>=2 and board[row-1][ind+1] == FOW and board[row-2][ind+2] == '.':
        #         kills += 1
        #         row -= 2
        #         ind += 2
        #     # left kill
        #     if ind>=2 and board[row-1][ind-1] == FOW and board[row-2][ind-2] == '.':
        #         kills+=1
        #         row-=2
        #         ind-=2
        # print(kills)
        # kill_list.append(kills)

    # def leftkill(row, ind, kills, board, FOW, N):
    #     # left kill
    #     if ind >= 2 and board[row - 1][ind - 1] == FOW and board[row - 2][ind - 2] == '.':
    #         kills += 1
    #         row -= 2
    #         ind -= 2
    #     return kills, row, ind
    #
    # def rightkill(row, ind, kills, board, FOW, N):
    #     # right kill
    #     if N - ind >= 2 and board[row - 1][ind + 1] == FOW and board[row - 2][ind + 2] == '.':
    #         kills += 1
    #         row -= 2
    #         ind += 2
    #     return kills, row, ind
    #
    # for r, i in reversed(indices):
    #     row = r
    #     ind = i
    #     kills = 0
    #     r,i,k = leftkill(row, ind, kills, board, FOW, N)
    #     print(r,i,k)
    #     while row > 1:
    #         flag = False
    #         if leftkill(row, ind, kills, board, FOW, N)[2] > rightkill(row, ind, kills, board, FOW, N)[2]:
    #             row, ind, kills = leftkill(row, ind, kills, board, FOW, N)
    #             flag = True
    #         else:
    #             row, ind, kills = rightkill(row, ind, kills, board, FOW, N)
    #             flag = True
    #         if not flag:
    #             row -= 1
    #
    #     kill_list.append(kills)


    return max(kill_list)

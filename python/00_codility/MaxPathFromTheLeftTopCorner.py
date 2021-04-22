"""
You are given a matrix A consisting of N rows and M columns, where each cell contains a digit. 
Your task is to find a continuous sequence of neighbouring cells, starting in the top-left corner and 
ending in the bottom-right corner (going only down and right), that creates the biggest possible integer 
by concatenation of digits on the path. By neighbouring cells we mean cells that have exactly one common side.

Write a function:

def solution(A)

that, given matrix A consisting of N rows and M columns, 
returns a string which represents the sequence of cells that we should pick to obtain the biggest possible integer.

e.g.
wih matrix:
9   9   7
9   7   2
6   9   5
9   1   2

function should return:
"997952" as, following path forms largest number
_____
9   9|   7
___  |
9  |7|   2
   | |___
6  |9   5|
   |___  |
9   1  |2| 
"""


def solution(a):
    # initialize first element
    num = []

    def recurse_on_equal(b, number):
        # get dimesions
        n = len(b)
        m = len(b[0])
        number.append(b[0][0])
        j, flag = 0, False

        for i in range(n - 1):
            while j < m - 1:
                if b[i][j + 1] > b[i + 1][j]:
                    j += 1
                    number.append(b[i][j])
                    flag = True
                    # C = [sublist[j+1:] for sublist in B]
                    # return recurse_on_equal(C, number)
                elif b[i][j + 1] < b[i + 1][j]:
                    i += 1
                    number.append(b[i][j])
                    # D = [sublist for sublist in B[i+1:]]
                    # return recurse_on_equal(D, number)
                else:
                    # C = B[i+1:,j:]
                    C = [sublist[j + 1:] for sublist in b]
                    # D = B[i:,j+1:]
                    D = [sublist for sublist in b[i + 1:]]
                    C_out = recurse_on_equal(C, number[:])
                    D_out = recurse_on_equal(D, number[:])
                    num_c = int("".join(map(str, C_out)))
                    num_d = int("".join(map(str, D_out)))
                    if num_c == num_d or num_c > num_d:
                        # number.extend(C_out)
                        return C_out
                    else:
                        # number.extend(D_out)
                        return D_out
                if not flag:
                    j += 1
        return number

    result = recurse_on_equal(a, num)
    result.append(a[-1][-1])
    return "".join(map(str, result))


if __name__ == '__main__':
    A = [
        [9, 9, 7],
        [9, 7, 2],
        [6, 9, 5],
        [9, 1, 2]
    ]

    print(solution(A))

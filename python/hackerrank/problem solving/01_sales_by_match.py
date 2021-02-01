"""
Alex works at a clothing store. There is a large pile of socks that must be paired by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

Function Description
Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock
Input Format

The first line contains an integer , the number of socks represented in .
The second line contains  space-separated integers describing the colors  of the socks in the pile.

Output Format
Return the total number of matching pairs of socks that Alex can sell.

Sample Input
9
10 20 20 10 10 30 50 10 20

Sample Output
3
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    # define dictionary for socks -->  socks_dict = {<sock_colour> : count}
    pairs_count, socks_dict = 0, {}
    # count number of socks for each colour
    for sock in ar:
        socks_dict.setdefault(sock, 0)
        socks_dict[sock] += 1
    # count number of pairs for each colour
    for value in socks_dict.values():
        pairs_count += value//2

    return pairs_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

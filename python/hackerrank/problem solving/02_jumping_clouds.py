"""
There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered  if they are safe or  if they must be avoided.

Example

Index the array from . The number on each cloud is its index in the list so the player must avoid the clouds at indices  and . They could follow these two paths:  or . The first path takes  jumps while the second takes . Return .

Function Description

Complete the jumpingOnClouds function in the editor below.

jumpingOnClouds has the following parameter(s):

int c[n]: an array of binary integers
Returns

int: the minimum number of jumps required
Input Format

The first line contains an integer , the total number of clouds. The second line contains  space-separated binary integers describing clouds  where .
Output Format

Print the minimum number of jumps needed to win the game.

Sample Input 0

7
0 0 1 0 0 1 0
Sample Output 0

4

Sample Input 1

6
0 0 0 0 1 0
Sample Output 1

3
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):
    # prune list from index 0 till list has single element left [i.e. reached top]
    # number of elements removed depends on height of jump  made : 1 or 2
    # increase jmup count for each jump
    jumps= 0
    while len(c) > 1:
        try:
            if c[2] == 0:
                jumps += 1
                del c[:2]
            elif c[1] == 0:
                jumps += 1
                del c[:1]
        # case when seconds last jump is of size 1, hence only 2 elements left.
        #  So, if c[2] == 0: throws IndexError
        except IndexError:
            if c[1] == 0:
                jumps += 1
                del c[:1]

    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

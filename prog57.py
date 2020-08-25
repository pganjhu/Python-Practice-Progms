# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 19:14:58 2020

@author: Pawan
"""
'''
The first line contains a single integer T, the number of test cases. For each test case, there are 2 lines. The first line of each test case contains , the number of cubes. The second line contains space separated integers, denoting the sideLengths of each cube in that order.

Constraints
1 <= T <= 5
1 <= n <= 10**5
1 <= sideLength <= 2**31
Output Format
For each test case, output a single line containing either "Yes" or "No" without the quotes.

Sample Input
2
6
4 3 2 1 3 4
3
1 3 2
Sample Output
Yes
No
Explanation
In the first test case, pick in this order: left - 4, right - 4, left - 3, right - 3, left - 2, right - 1. In the second test case, no order gives an appropriate arrangement of vertical cubes. 3 will always come after either 1 or 2.'''
if __name__ == '__main__':
    num_tests = int(input().strip())

    for _ in range(num_tests):
        num_cubes = int(input().strip())
        cube_sidelengths = list(map(int, map(str.strip, input().strip().split())))


        i, j = 0, len(cube_sidelengths)-1
        pile = []

        while i != j:
            left, right = cube_sidelengths[i], cube_sidelengths[j]
            # In case there is nothing in the pile just add the bigger one
            if not pile:
                if left > right:
                    pile.append(left)
                    i += 1
                else:
                    pile.append(right)
                    j -= 1
            else:
                # Take the bigger of the left and right element and compare it
                # to the last item on the pile. If it's bigger we can't pile
                # it up, otherwise put it on the pile and continue
                if left > right:
                    if left > pile[-1]:
                        print('No')
                        break
                    else:
                        pile.append(left)
                        i += 1
                else:
                    if right > pile[-1]:
                        print('No')
                        break
                    else:
                        pile.append(right)
                        j -= 1
        else:
            print('Yes')

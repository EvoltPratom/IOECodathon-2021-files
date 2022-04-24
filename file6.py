import math
import file5


def solve(arr, queries):
    # Write your code here
    resu = []
    for i in queries:
        if arr[i[0] - 1] % 2 == 0:
            resu.append("Even")
        else:
            resu.append("Odd")
    return resu


# print(solve([3, 2, 7], [[1, 2], [2, 3]]))

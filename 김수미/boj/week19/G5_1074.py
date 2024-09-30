'''
 * Author    : Kim Su Mi
 * Date      : 2024.09.30(MON)
 * Runtime   : 32 ms
 * Memory    : 31120 KB
 * Algorithm : Divide-and-conquer
'''

import sys
N, r, c = map(int, sys.stdin.readline().split())

res = 0
while N != 0:
    # 4등분으로 분할
    N -= 1
    if r < 2**N and c < 2**N:
        res += 0

    elif r < 2**N and c >= 2**N:
        res += (2**N) * (2**N) * 1
        c -= (2**N)

    elif r >= 2**N and c < 2**N:
        res += (2**N) * (2**N) * 2
        r -= (2**N)

    else:
        res += (2**N) * (2**N) * 3
        r -= (2**N)
        c -= (2**N)

print(res)
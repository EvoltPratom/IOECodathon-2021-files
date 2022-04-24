import math


def minimumBribes(q):
    # Write your code here # wrong right now
    l = len(q)
    count = 0
    c = []
    for i in range(1, l + 1):
        # get the diff with
        cc = abs(i - q[i - 1])
        c.append(cc)
        print(c)
        if cc > 2:
            return "Too Chaotic"
        count += cc
    print(c)
    return count // 2


def divisors(n):
    # even divisors of n, fastest method
    if n % 2 == 1:  # if n is odd return 0
        return 0

    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):  # looping through even nos
        # print(i)
        if i == 0:
            continue
        if n % i == 0 and i % 2 == 0:
            count += 1

        if n % (n // i) == 0 and (n // i) % 2 == 0:
            count += 1

        if i == n // i and i % 2 == 0 and n % i == 0:
            count -= 1
    return count


# print(minimumBribes([2, 1, 5, 3, 4]))

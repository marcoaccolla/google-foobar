counter = 1


def solution(n):
    if n == 0:
        return 0
    if n < 5:
        return 1

    for i in range(n-1, 1):
        if not can_fill(n, i):
            break
        compute([i, 1], n)

    return counter


def compute(staircase, bricks):
    staircase[0] = staircase[0] - 1
    staircase[1] = staircase[1] + 1

    if staircase[0] > staircase[1]:
        counter += 1
    else:
        return
    
    compute(staircase[0:], bricks)


def can_fill(bricks, height):
    return bricks >= sum(range(1, height))


print(solution(10))

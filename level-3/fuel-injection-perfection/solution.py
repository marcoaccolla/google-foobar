def solution(n):
    n = int(n)
    result = 0
    while n > 3:
        if n % 2 != 0:
            result += 1
            if (n + 1) % 4 == 0:
                n += 1
            else:
                n -= 1
        n = n / 2
        result += 1

    if n == 3:
        result += 2
    elif n == 2:
        result += 1

    return result


print(solution('89'))

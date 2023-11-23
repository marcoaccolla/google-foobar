def solution(x, y):
    return (set(x) - set(y)).union(set(y) - set(x)).pop()


print(solution([5], [2]))

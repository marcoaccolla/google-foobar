def solution(xs):
    xs.sort()
    has_neutral = 0 in xs
    positives = list(filter(lambda n: n > 0, xs))
    negatives = list(filter(lambda n: n < 0, xs))

    if len(positives) == 0 and len(negatives) < 2:
        if len(negatives) == 1 and has_neutral:
            return '0'
        else:
            return str(negatives[0])

    if (len(negatives) % 2) != 0:
        negatives.pop()

    energy = 1
    for pos in positives:
        energy *= pos

    for neg in negatives:
        energy *= neg

    return str(energy)


print(solution([0, -1]))

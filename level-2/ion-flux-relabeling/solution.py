import math


def solution(h, q):
    tree = create_tree(h)
    result = [find_flux(tree, x) for x in q]
    return result


def find_flux(tree, index):
    # now find the flux above the one requested
    # search in every level
    result = 0
    for i, level in enumerate(tree):
        # get the index
        pos = level.index(index) if index in level else -1
        # if we found the flux in the root-level we return -1
        if pos == -1:
            continue

        if i == 0:
            result = -1
        # else we get the index of the level above by dividing down the position of the flux by 2
        else:
            result = tree[i - 1][int(math.floor(pos / 2))]

    return result


def create_tree(h):
    tree = []
    pattern = [[1]]

    # create leaf-level pattern
    for i in range(2, h):
        curr_list = pattern[0][:]
        pattern[0].append(i)
        pattern[0].extend(curr_list)

    # expand on the levels above
    for i in range(0, h - 2):
        # filter out '1', we don't need them to populate levels
        odd = pattern[i][1::2]
        # value + 2^i-1
        odds = map(lambda x: x + pow(2, i + 1) - 1, odd)
        pattern.append(list(odds))

    # populate perfect binary tree
    for i in range(1, h):
        # for each level start from the first elem: 2^i-1
        tree.append([pow(2, i) - 1])
        # now sum all the values from the pattern, with every sum you get a new element of the tree
        for index, value in enumerate(pattern[i - 1]):
            tree[i - 1].append(tree[i - 1][index] + value)

    # append the root
    tree.append([pow(2, h) - 1])
    # reverse the tree just to have the root as first elem
    tree.reverse()

    return tree


print(solution(5, [19, 14, 28]))
print(solution(3, [7, 3, 5, 1]))

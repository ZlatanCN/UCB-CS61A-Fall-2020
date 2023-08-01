def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    else:
        return max(height(branch) for branch in branches(t)) + 1


def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """

    def max_path_sum_helper(t, max_path=0):
        if is_leaf(t):
            return label(t) + max_path
        else:
            return max([max_path_sum_helper(b, label(t)) for b in branches(t)])

    return max_path_sum_helper(t)


def square_tree(t):
    """Return a tree with the square of every element in t
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
      4
        9
        16
      25
        36
          49
        64
    """
    if is_leaf(t):
        return tree(label(t) ** 2, [])
    else:
        new_branches = [square_tree(b) for b in branches(t)]
        return tree(label(t) ** 2, new_branches)


def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if label(tree) == x:
        return [label(tree)]
    else:
        for b in branches(tree):
            path = find_path(b, x)
            if path:
                return [label(tree)] + path
    return None


def prune_binary(t, nums):
    """
    >>> t = tree('1', [tree('0', [tree('0'), tree('1')]), tree('1', [tree('0')])])
    >>> t_new = prune_binary(t,  ['01', '110', '100'])
    >>> print_tree(t_new)
    1
      0
        0
      1
        0
    """
    if is_leaf(t):
        if label(t) in nums:
            return t
        return None
    else:
        next_valid_nums = [num[1:] for num in nums if num.startswith(label(t))]
        new_branches = []
        for b in branches(t):
            pruned_branch = prune_binary(b, next_valid_nums)
            if pruned_branch is not None:
                new_branches.append(pruned_branch)
        if not new_branches:
            return None
        return tree(label(t), new_branches)


# Tree ADT


def tree(label, branches=[]):
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)


def label(tree):
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]


def branches(tree):
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]


def is_tree(tree):
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True


def is_leaf(tree):
    return not branches(tree)


def change_abstraction(change):
    change_abstraction.changed = change


change_abstraction.changed = False


def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def copy_tree(t):
    return tree(label(t), [copy_tree(b) for b in branches(t)])

def lexi_sort(arr, lexi):
    """ Return a sorted list based on the lexicographic ordering passed in

    >>> lexi_sort(['acb', 'abc', 'bca'], 'abc')
    ['abc', 'acb', 'bca']

    >>> lexi_sort(['acb', 'abc', 'bca', 'bca'], 'cba')
    ['bca', 'bca', 'acb', 'abc']

    >>> lexi_sort(['aaa','aa',''], 'a')
    ['', 'aa', 'aaa']
    """

    order = [None] * len(lexi)
    for i, v in enumerate(lexi):
        order[ord(v) - 97] = i
    return bucket_sort(arr, order, 0)

def bucket_sort(arr, order, place):
    """ Helper function that sorts starting on a certain character """

    buckets = [[] for x in xrange(len(order))];
    first = [];
    for w in arr:
        if len(w) == place:
            first.append(w)
        else:
            buckets[order[ord(w[place]) - 97]].append(w)
    for i, v in enumerate(buckets):
        if not len(v) == 0:
            buckets[i] = bucket_sort(v, order, place + 1)
    
    return first + reduce(lambda a, b: a + b, buckets)

if __name__ == '__main__':
    import doctest
    if doctest.testmod()[0] == 0:
        print 'All tests passed'
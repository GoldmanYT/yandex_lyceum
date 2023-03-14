def count_chars(s):
    if type(s) != str:
        raise TypeError('Expected str, got {}'.format(type(s)))

    return dict((i, s.count(i)) for i in set(s))

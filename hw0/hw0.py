def funky_sum(a, b, mix):
    """
    Returns the weighted sum of `a` and `b`, using
    `mix` as the weight for `b` and 1 - `mix` as the
    weight for `a`.

    If `mix` < 0, uses `mix` = 0.
    If `mix` > 1, uses `mix` = 1.
    """
    mix = max(0, mix)
    mix = min(1, mix)
    return (1 - mix) * a + mix * b


def total(n):
    """
    Returns the `n`th triangular number.
    If `n` < 0, returns None.
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


def swip_swap(src, c1, c2):
    """
    Returns a string identical to `src` except each
    occurrence of `c1` is swapped with `c2` and
    vice versa.
    """
    ret = ""
    for c in src:
        if c == c1:
            ret += c2
        elif c == c2:
            ret += c1
        else:
            ret += c
    return ret

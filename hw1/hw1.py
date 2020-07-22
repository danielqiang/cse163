def total(n):
    """
    Returns the sum of the numbers from 0 to n (inclusive).
    If n is negative, returns None.
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


# Write your functions here!

def count_divisible_digits(n: int, m: int) -> int:
    """
    Returns the number of digits in `m` that are divisible
    by `n`. If `m` is 0, returns 0. Assumes `m` is non-negative.
    """
    if m == 0:
        return 0
    count = 0
    for digit in str(n):
        if not digit.isnumeric():
            continue
        if int(digit) % m == 0:
            count += 1
    return count


def is_relatively_prime(n: int, m: int) -> bool:
    """
    Returns True if `n` and `m` are coprime, False otherwise.
    """
    if m > n:
        n, m = m, n
    while m != 0:
        n, m = m, n % m
    return n == 1


def travel(s: str, x: int, y: int) -> tuple:
    """
    Given (`x`, `y`) as starting coordinates, return
    the new position (x_new, y_new) after directions given by each
    character in `s`.
    The following characters are recognized:
        - 'n': y += 1.
        - 's': y -= 1.
        - 'w': x -= 1.
        - 'e': x += 1
    Ignores case and unrecognized characters.
    """
    for c in s.lower():
        if c == 'n':
            y += 1
        elif c == 's':
            y -= 1
        elif c == 'w':
            x -= 1
        elif c == 'e':
            x += 1
    return x, y


def compress(s: str) -> str:
    """
    Performs a variant of run-length-encoding, returning
    a new string such that each character is followed by its
    count and any duplicate characters are removed.
    """
    if len(s) == 0:
        return ''

    i, j = 0, 1
    cur_count = 1
    res = ""
    while j < len(s):
        if s[i] != s[j]:
            res += s[i] + str(cur_count)
            cur_count = 1
            i = j
        else:
            cur_count += 1
        j += 1
    return res + s[-1] + str(cur_count)


def _max(iterable, *, key=lambda x: x):
    """
    Barebones functional equivalent of `max()` builtin,
    since I don't think we've learned max() yet?

    Assumes that the iterable is non-empty and that `key`
    is a callable which returns a numeric type. If there is a tie,
    returns the first occurrence.
    """
    __max, key_max = None, float('-inf')
    for i in iterable:
        key_val = key(i)
        if key_val > key_max:
            __max = i
            key_max = key_val
    return __max


def longest_line_length(file_name: str):
    """
    Returns the length of the longest line in
    `file_name` (including whitespace).
    If the file is empty, returns None.
    """
    with open(file_name) as f:
        lines = f.readlines()
        if len(lines) == 0:
            return None
        return _max(len(line) for line in lines)


def longest_word(file_name: str):
    """
    Returns a string indicating the length of the longest
    word in `file_name` and the line it appeared on.
    The string has the following format:
        '<line no.>: <longest word>'
    If the file is empty, returns None.
    """
    with open(file_name) as f:
        lines = f.readlines()
        if len(lines) == 0:
            return None
        words = ((word, i)
                 for i, line in enumerate(lines, start=1)
                 for word in line.split())
        longest, lineno = _max(words, key=lambda tup: len(tup[0]))
        return str(lineno) + ': ' + str(longest)


def get_average_in_range(ls: list, low: int, high: int):
    """
    Returns the average of all elements e in `ls` satisfying
    low <= e < high. If no elements satisfy this constraint,
    return 0.
    """
    cur_sum, count = 0, 0
    for e in ls:
        if low <= e < high:
            cur_sum += e
            count += 1
    if count > 0:
        return cur_sum / count
    return 0


def mode_digit(n: int):
    """
    Returns the most common digit in `n`. If there is a tie,
    returns the digit with a highest numeric value.
    """
    counter = {}
    if n < 0:
        n = -n
    for c in str(n):
        c = int(c)
        if c not in counter:
            counter[c] = 0
        counter[c] += 1
    mode, max_count = 0, 0
    for k, v in counter.items():
        if v >= max_count:
            mode = k if k > mode else mode
            max_count = v
    return mode

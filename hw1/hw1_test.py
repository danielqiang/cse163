import hw1

from cse163_utils import assert_equals


def test_total():
    """
    Tests the total method
    """
    # The regular case
    assert_equals(15, hw1.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, hw1.total(1))
    assert_equals(0, hw1.total(0))

    # Test the None case
    assert_equals(None, hw1.total(-1))


def test_count_divisible_digits():
    assert_equals(4, hw1.count_divisible_digits(650899, 3))
    assert_equals(1, hw1.count_divisible_digits(-204, 5))
    # new tests
    assert_equals(0, hw1.count_divisible_digits(0, 0))
    assert_equals(3, hw1.count_divisible_digits(333, 3))


def test_is_relatively_prime():
    assert_equals(True, hw1.is_relatively_prime(12, 13))
    assert_equals(False, hw1.is_relatively_prime(12, 14))
    # new tests
    assert_equals(True, hw1.is_relatively_prime(1, 1))
    assert_equals(True, hw1.is_relatively_prime(1, 10))


def test_travel():
    assert_equals((-1, 4), hw1.travel('NW!ewnW', 1, 2))
    # new tests
    assert_equals((0, 0), hw1.travel('', 0, 0))
    assert_equals((0, 0), hw1.travel('!!!!!!!', 0, 0))


def test_compress():
    assert_equals('c1o17l1k1a1n1g1a1r1o2',
                  hw1.compress('cooooooooooooooooolkangaroo'))
    # new tests
    assert_equals('c1', hw1.compress('c'))
    assert_equals('a8', hw1.compress('aaaaaaaa'))


def test_longest_line_length():
    assert_equals(35, hw1.longest_line_length('song.txt'))
    # new tests
    assert_equals(None, hw1.longest_line_length('empty.txt'))
    assert_equals(5, hw1.longest_line_length('tie.txt'))


def test_longest_word():
    assert_equals('3: Merrily,', hw1.longest_word('song.txt'))
    # new tests
    assert_equals(None, hw1.longest_word('empty.txt'))
    assert_equals('1: asdf', hw1.longest_word('tie.txt'))


def test_get_average_in_range():
    assert_equals(5.5, hw1.get_average_in_range([1, 5, 6, 7, 9], 5, 7))
    # new tests
    assert_equals(0, hw1.get_average_in_range([], 10, 20))
    assert_equals(0, hw1.get_average_in_range([1, 2, 3], 4, 6))


def test_mode_digit():
    assert_equals(1, hw1.mode_digit(12121))
    # new tests
    assert_equals(3, hw1.mode_digit(2233))
    assert_equals(1, hw1.mode_digit(1))
    assert_equals(1, hw1.mode_digit(-1))


def main():
    test_total()
    test_count_divisible_digits()
    test_is_relatively_prime()
    test_travel()
    test_compress()
    test_longest_line_length()
    test_longest_word()
    test_get_average_in_range()
    test_mode_digit()


if __name__ == '__main__':
    main()

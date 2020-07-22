import hw0

from cse163_utils import assert_equals


def test_total():
    # The regular case
    assert_equals(15, hw0.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, hw0.total(1))
    assert_equals(0, hw0.total(0))
    # Special case: n < 0
    assert_equals(None, hw0.total(-1))


def test_funky_sum():
    # matches spec
    assert_equals(2, hw0.funky_sum(1, 3, 0.5))
    assert_equals(1, hw0.funky_sum(1, 3, 0))
    assert_equals(1.5, hw0.funky_sum(1, 3, 0.25))
    # new tests
    assert_equals(1, hw0.funky_sum(1, 3, -1))
    assert_equals(3, hw0.funky_sum(1, 3, 5))


def test_swip_swap():
    # matches spec
    assert_equals('offbar', hw0.swip_swap('foobar', 'f', 'o'))
    assert_equals('foocar', hw0.swip_swap('foobar', 'b', 'c'))
    assert_equals('foobar', hw0.swip_swap('foobar', 'z', 'c'))
    # new tests
    assert_equals('foobar', hw0.swip_swap('fllbar', 'l', 'o'))
    assert_equals('', hw0.swip_swap('', 'a', 'b'))


def main():
    test_total()
    test_funky_sum()
    test_swip_swap()


if __name__ == '__main__':
    main()

import pandas as pd

# Don't worry about this import syntax, we will talk about it later
# You can call the method using
#    assert_equals(expected, received)
#    parse(file)
from cse163_utils import assert_equals, parse

import hw2_manual
import hw2_pandas

# Pre-load test files
_pokemon_test = parse('pokemon_test.csv')
_pokemon_test_df = pd.read_csv('pokemon_test.csv')
_empty = parse('empty.csv')
_empty_df = pd.read_csv('empty.csv')
_single = parse('single.csv')
_single_df = pd.read_csv('single.csv')


# This file is left blank for you to fill in with your tests!
def test_species_count():
    # manual
    assert_equals(3, hw2_manual.species_count(_pokemon_test))
    assert_equals(0, hw2_manual.species_count(_empty))
    # pandas
    assert_equals(3, hw2_pandas.species_count(_pokemon_test_df))
    assert_equals(0, hw2_pandas.species_count(_empty_df))


def test_max_level():
    # manual
    assert_equals(('Lapras', 72), hw2_manual.max_level(_pokemon_test))
    assert_equals(('Persian', 40), hw2_manual.max_level(_single))
    # pandas
    assert_equals(('Lapras', 72), hw2_pandas.max_level(_pokemon_test_df))
    assert_equals(('Persian', 40), hw2_pandas.max_level(_single_df))


def test_filter_range():
    # manual
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_manual.filter_range(_pokemon_test, 30, 70))
    assert_equals([], hw2_manual.filter_range(_pokemon_test, -10, 0))
    # pandas
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_pandas.filter_range(_pokemon_test_df, 30, 70))
    assert_equals([], hw2_pandas.filter_range(_pokemon_test_df, -10, 0))


def test_mean_attack_for_type():
    # manual
    assert_equals(47.5, hw2_manual.mean_attack_for_type(
        _pokemon_test, 'fire'))
    assert_equals(None, hw2_manual.mean_attack_for_type(
        _pokemon_test, 'asdf'))
    # pandas
    assert_equals(47.5, hw2_pandas.mean_attack_for_type(
        _pokemon_test_df, 'fire'))
    assert_equals(None, hw2_pandas.mean_attack_for_type(
        _pokemon_test_df, 'asdf'))


def test_count_types():
    # manual
    assert_equals({'fire': 2, 'water': 2},
                  hw2_manual.count_types(_pokemon_test))
    assert_equals({'normal': 1}, hw2_manual.count_types(_single))
    # pandas
    assert_equals({'fire': 2, 'water': 2},
                  hw2_pandas.count_types(_pokemon_test_df))
    assert_equals({'normal': 1}, hw2_pandas.count_types(_single_df))


def test_highest_stage_per_type():
    # manual
    assert_equals({'fire': 2, 'water': 2},
                  hw2_manual.highest_stage_per_type(_pokemon_test))
    assert_equals({'normal': 2}, hw2_manual.highest_stage_per_type(_single))
    # pandas
    assert_equals({'fire': 2, 'water': 2},
                  hw2_pandas.highest_stage_per_type(_pokemon_test_df))
    assert_equals({'normal': 2}, hw2_pandas.highest_stage_per_type(_single_df))


def test_mean_attack_per_type():
    # manual
    assert_equals({'fire': 47.5, 'water': 140.5},
                  hw2_manual.mean_attack_per_type(_pokemon_test))
    assert_equals({'normal': 104}, hw2_manual.mean_attack_per_type(_single))
    # pandas
    assert_equals({'fire': 47.5, 'water': 140.5},
                  hw2_pandas.mean_attack_per_type(_pokemon_test_df))
    assert_equals({'normal': 104}, hw2_pandas.mean_attack_per_type(_single_df))


def main():
    test_species_count()
    test_max_level()
    test_filter_range()
    test_mean_attack_for_type()
    test_count_types()
    test_highest_stage_per_type()
    test_mean_attack_per_type()


if __name__ == '__main__':
    main()

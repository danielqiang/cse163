import pandas as pd
import math


# Write your functions here!
def species_count(data: pd.DataFrame):
    """
    Counts the number of unique Pokemon species
    in `data`.
    """
    return len(data['name'].unique())


def max_level(data: pd.DataFrame):
    """
    Returns a tuple of (`name`, `level`) where `name` is the name
    of the Pokemon with the highest level in `data` and `level`
    is its level.
    """
    _max = data.loc[data['level'].idxmax()]
    return _max['name'], _max['level']


def filter_range(data: pd.DataFrame, low, high):
    """
    Returns a list of all Pokemon names that have a range within
    [low, high).
    """
    in_range = data[data['level'].between(low, high - 1)]
    return in_range['name'].to_list()


def mean_attack_for_type(data: pd.DataFrame, pokemon_type):
    """
    Returns the average attack stat for all Pokemon in `data`
    with type `pokemon_type`.
    """
    avg = data[data['type'] == pokemon_type]['atk'].mean()
    if math.isnan(avg):
        return None
    return avg


def count_types(data: pd.DataFrame):
    """
    Returns a counter dict of Pokemon types in `data`.
    """
    return data.groupby('type').size().to_dict()


def highest_stage_per_type(data: pd.DataFrame):
    """
    Returns a dict mapping each type of Pokemon to the highest stage
    reached by that Pokemon type in `data`.
    """
    return data.groupby('type').max()['stage'].to_dict()


def mean_attack_per_type(data: pd.DataFrame):
    """
    Returns a dict mapping each type of pokemon to the average attack
    value of that Pokemon type in `data`.
    """
    return data.groupby('type').mean()['atk'].to_dict()

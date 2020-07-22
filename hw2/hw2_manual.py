# Write your solutions here!
def species_count(data):
    """
    Counts the number of unique Pokemon species
    in `data`.
    """
    unique_species = {d['name'] for d in data}
    return len(unique_species)


def max_level(data):
    """
    Returns a tuple of (`name`, `level`) where `name` is the name
    of the Pokemon with the highest level in `data` and `level`
    is its level.
    """
    levels = ((d['name'], d['level']) for d in data)
    return max(levels, key=lambda t: t[1])


def filter_range(data, low, high):
    """
    Returns a list of all Pokemon names that have a range within
    [low, high).
    """
    return [d['name'] for d in data
            if low <= d['level'] < high]


def mean_attack_for_type(data, pokemon_type):
    """
    Returns the average attack stat for all Pokemon in `data`
    with type `pokemon_type`.
    """
    attack_values = [d['atk'] for d in data
                     if d['type'] == pokemon_type]
    if len(attack_values) > 0:
        return sum(attack_values) / len(attack_values)
    return None


def count_types(data):
    """
    Returns a counter dict of Pokemon types in `data`.
    """
    types = {}
    for d in data:
        _type = d['type']
        if _type not in types:
            types[_type] = 0
        types[_type] += 1
    return types


def highest_stage_per_type(data):
    """
    Returns a dict mapping each type of Pokemon to the highest stage
    reached by that Pokemon type in `data`.
    """
    max_stages = {}
    for d in data:
        _type = d['type']
        cur_best = max_stages.get(_type, float('-inf'))
        max_stages[_type] = max(d['stage'], cur_best)
    return max_stages


def mean_attack_per_type(data):
    """
    Returns a dict mapping each type of pokemon to the average attack
    value of that Pokemon type in `data`.
    """
    ret = {}
    for d in data:
        _type = d['type']
        if _type not in ret:
            ret[_type] = [0, 0]
        ret[_type][0] += d['atk']
        ret[_type][1] += 1
    return {k: v[0] / v[1] for k, v in ret.items()}

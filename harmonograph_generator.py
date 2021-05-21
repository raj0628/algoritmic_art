from math import pi

harmonograph_values = {"Pattern 1": (3, 0, 2, 0, 0, 0, 0, 0), "Pattern 2": (3, 1, 3, 1, 0, 0, pi / 2, pi / 2),
                       "Pattern 3": (15, 1, 15, 1, 0, pi / 2, pi / 2, 0)}


def graph_selector(name=''):
    for ans in harmonograph_values:
        if name == ans:
            return harmonograph_values[ans]
        else:
            pass

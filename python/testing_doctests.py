import pandas as pd
import numpy as np

# Doc Tests
# ================================================

def sum(x, y):
    """ Function that sums together two numbers

    >>> sum(4, 10)
    14
    >>> sum(5, -2)
    3
    """
    return x + y


def abc(x, m):
    """ ...

    >>> x = np.ones(3)
    >>> m = np.eye(3)
    >>> list(abc(x, m))
    [1.0, 1.0, 1.0]
    """
    return x @ m


import doctest
doctest.testmod()

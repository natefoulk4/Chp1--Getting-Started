""" Tests the mathematical functions defined in demo/trial.py
"""

import pytest

def.test_square():
    """Tests the squaring function"""

    from demo.trial import square

    assert 4 == square(2)

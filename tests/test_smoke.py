from app import dot
import pytest

def test_dot():

    tol = 1e-9

    x = (1,1)
    y = (-1,-1)

    prod = dot(x, y)

    assert isinstance(prod, int) or isinstance(prod, float)

    assert abs(dot((1,2), (2,-1))) < tol

    assert dot((1,2), (1,2)) > tol

    assert dot((1,2), (-1,-2)) < tol 

    with pytest.raises(ValueError):
        dot((1,1,1), (1,1))

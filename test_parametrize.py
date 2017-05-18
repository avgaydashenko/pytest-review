import pytest

@pytest.mark.parametrize('numiter', range(10))
def test_func(numiter):
  assert numiter < 9

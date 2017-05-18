import time
import pytest

@pytest.mark.parametrize('x', range(5))
def test_xdist(x):
  time.sleep(x)

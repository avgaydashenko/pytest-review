def test_function(myfuncarg):
  assert myfuncarg == 17

def pytest_funcarg__myfuncarg(request):
  return 42

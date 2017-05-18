from test_foo import Foo

def pytest_assertrepr_compare(op, left, right):
  if isinstance(left, Foo) and isinstance(right, Foo) and op == '==':
    return ['Comparing Foo val attributes:',
            '    vals: %s != %s' % (left.val, right.val)]

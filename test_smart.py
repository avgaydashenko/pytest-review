def test_list_compare():
  l = list(range(10))
  l2 = list(range(5)) + list(range(7, 10))
  assert l == l2
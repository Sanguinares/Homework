def test_sets_diff(st, st1):
    assert 'zero' not in st.difference(st1)

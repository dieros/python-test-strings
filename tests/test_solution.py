from solution.solution import solution


def test_one_digram_long_string():
    assert solution('aakmaakmakda') == 7


def test_one_digram_extra_long_string():
    assert solution('abacabadabacaba') == 12


def test_one_digram_short_string():
    assert solution('aaa') == 1
    

def test_no_digram():
    assert solution('something') == -1

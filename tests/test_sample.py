import timestack


def test_pass():
	assert timestack.base.math_func(3) == 4


def test_fail():
	assert timestack.base.math_func(3) != 5

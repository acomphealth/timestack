def func(x):
	return x + 1


def test_pass():
	assert func(3) == 4


def test_fail():
	assert func(3) == 5

from context import timestack


def test_pass():
	assert timestack.func(3) == 4


def test_fail():
	assert timestack.func(3) != 5

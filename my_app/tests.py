from my_app.sum import sum
from my_app.views import index

def test_sum():
	assert sum(1, 1) == 2
	assert sum(1, 2) == 3


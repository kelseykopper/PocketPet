init:
	pip install -U pygame==2.5.1 --user
test:
	py.test tests

.PHONY: init test
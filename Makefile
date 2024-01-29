run:
	python3 pet.py 

test: 
	python3 tests.py

setup: requirements.txt
	pip install -r requirements

clean:
	rm -rf __pycache__

.PHONY: run clean test

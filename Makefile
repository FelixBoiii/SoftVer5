test:
	uv run test_generator.py curling.py 1000
	uv run coverage run --branch -m unittest
	uv run coverage html
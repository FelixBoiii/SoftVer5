test:
	uv run test_generator.py curling.py 100
	uv run coverage run --branch -m unittest
	uv run coverage html
install:
	poetry install

brain-games:
	poerty run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall
	
lint:
	poetry run flake8 brain_games
	
brain-even:
	poetry run brain-even

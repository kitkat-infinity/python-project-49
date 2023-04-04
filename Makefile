install:
	poetry install

brain-games:
	poerty run brain-games

build:
	poetry build

publish:
	poetry publish

package-install:
	python3 -m pip install --user dist/*.whl

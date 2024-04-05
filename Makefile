install:
	cd docker && \
	docker compose up --build

clean:
	rm -rf __pycache__ dist kgcreator.egg-info build
	rm -rf kgcreator/__pycache__ tests/__pycache__

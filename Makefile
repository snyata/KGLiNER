install:
	cd docker && \
	docker compose up --build

clean:
	rm -rf __pycache__ dist kgliner.egg-info build
	rm -rf kgliner/__pycache__ tests/__pycache__

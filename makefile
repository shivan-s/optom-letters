.PHONY: run
run:
	@echo "Running..."
	docker-compose -f ./docker/dev/docker-compose.yml down --remove-orphans
	docker-compose -f ./docker/dev/docker-compose.yml up --build

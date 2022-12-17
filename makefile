.PHONY: run
run:
	@echo "Running..."
	docker-compose -f ./docker/dev/docker-compose.yml down --remove-orphans
	docker-compose -f ./docker/dev/docker-compose.yml up --build

.PHONY: deploy
deploy:
	@echo "Deploying application" && \
	ansible-playbook ansible/deploy.yml -i ansible/hosts -K

# quick deploy does not run certbot or nginx
.PHONY: quick-deploy
quick-deploy:
	@echo "Quickly deploying application" && \
	ansible-playbook ansible/quick-deploy.yml -i ansible/hosts -K

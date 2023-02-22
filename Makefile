DOCKER_COMPOSE_DEV := docker-compose -f docker/development/docker-compose.yml

start-development:
	$(DOCKER_COMPOSE_DEV) up -d

stop-development:
	$(DOCKER_COMPOSE_DEV) down
DOCKER_COMPOSE_DEV := docker-compose -f docker/development/docker-compose.yml

# make start-development
# make start-development -- --build
start-development:
	@if [ "$(filter --build,$(MAKECMDGOALS))" != "" ]; then \
		$(DOCKER_COMPOSE_DEV) build; \
	fi
	$(DOCKER_COMPOSE_DEV) up -d

migrate-development:
	$(DOCKER_COMPOSE_DEV) exec flask_ms python .vscode/scripts/set_password.py
	FLASK_APP=manage.py FLASK_DEBUG=1 $(DOCKER_COMPOSE_DEV) exec -e FLASK_APP=manage.py -e FLASK_DEBUG=1 flask_ms flask db upgrade

stop-development:
	$(DOCKER_COMPOSE_DEV) stop
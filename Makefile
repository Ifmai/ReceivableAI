COMPOSE_FILES := -f docker-compose.yml


up:
	@sudo docker compose $(COMPOSE_FILES) up -d 

build:
	@sudo docker compose $(COMPOSE_FILES) up -d --build

down:
	@docker compose $(COMPOSE_FILES) down

fclean: down
	@docker system prune -a -f
	@docker volume prune -f
	@docker network prune -f
	@docker compose $(COMPOSE_FILES) down --volumes --remove-orphans

re: down up

fre: fclean build

.PHONY: all fre re down clean
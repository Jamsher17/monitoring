# Variable
BASE = -f docker-compose.yml

# Commands
.PHONY: migrate makemigrations superuser up

# Apply database migrations
migrate:
	docker-compose $(BASE) run --rm backend python manage.py migrate

# Create new database migrations
makemigrations:
	docker-compose $(BASE) run --rm backend python manage.py makemigrations

# Create a superuser
superuser:
	docker-compose $(BASE) run --rm backend python manage.py createsuperuser

# Build and start Docker containers in detached mode
up:
	docker-compose $(BASE) up --build -d

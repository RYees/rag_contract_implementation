.PHONY: build run clean

up:
	docker compose up 

stop:
	docker compose stop

down:
	docker compose down

clean:
	docker rmi $(docker images -q)
	docker volume rm $(docker volume ls -q)
	docker network rm $(docker network ls -q) 
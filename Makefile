docker:
	@echo "---- Building & Up Container ----"
	@docker-compose down
	#@docker-compose build	
	@docker-compose up -d
	@echo "---- EndPoints ----"
	@echo "---- http://127.0.0.1:8088/task     ----"
	@echo "---- http://127.0.0.1:8088/schedule ----"
	@echo "---- http://127.0.0.1:8088/retry    ----"

dockerdown:
	@docker-compose down

setup:
	@echo "---- Setting Enviroment ----"
	@virtualenv env
	@. env/bin/activate
	@echo "---- Installing Python dependencies ----"
	@pip3 install -r requirements.txt --upgrade

run_workers:
	huey_consumer src.main.huey -k greenlet -w 2

run_worker:
	PYTHONPATH="$(pwd)" python venv/lib/python3.7/site-packages/huey/bin/huey_consumer.py src.main.huey

run:
	PYTHONPATH="/srv" python src/main.py

run_all:
	@make run & make run_workers
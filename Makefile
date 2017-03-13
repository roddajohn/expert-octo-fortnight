# Make file -- look at default for explanation

default:
	@echo "Examples:"
	@echo "    make run          # Starts a Flask development server locally"
	@echo "    make clean        # Cleans all directors"
	@echo "    make test         # Runs unit tests"
	@echo "    make mongo        # Starts a mongo server"

setup:
	virtualenv env
	. env/bin/activate
	pip install -r requirements.txt
	export PYTHONPATH='.'
	mkdir data

run:
	./manage.py devserver -p 5000

clean:
	rm -r *~

test:	
	py.test --cov-report html --cov app tests

mongo:
	mongod --httpinterface --dbpath data --rest



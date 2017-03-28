default:
	@echo "Examples:"
	@echo "    make run          # Starts a Flask development server locally"
	@echo "    make clean        # Cleans all directors"
	@echo "    make test         # Runs unit tests"

setup:
	virtualenv env
	. env/bin/activate
	pip install -r requirements.txt

run:
	./manage.py devserver -p 5000

clean:
	rm -r *~

test:	
	py.test --cov-report html --cov app tests

default:
	@echo "Examples:"
	@echo "    make run          # Starts a Flask development server locally"
	@echo "    make production   # Starts the production server, sets up logging to logs/"
	@echo "    make clean        # Cleans all directors"
	@echo "    make test         # Runs unit tests"
	@echo "    make rst          # Autogenerates Sphinx documentation for any new files that may have been added since last autodoc run"

setup:
	virtualenv env
	. env/bin/activate
	pip install -r requirements.txt

run:
	./manage.py devserver -p 5000

production:
	./manage.py --config_prod -p 5000 -l logs devserver

clean:
	rm -r *~

test:	
	py.test --cov-report html --cov app tests

rst:
	sphinx-apidoc -f -o docs/source/ app/

# Make file -- look at default for explanation

default:
	@echo "Examples:"
	@echo "    make run              # Starts a Flask development server locally"
	@echo "    make clean            # Cleans all directors"
	@echo "    make test             # Runs unit tests"
	@echo "    make createdb         # Creates the SQL database"
	@echo "    make createdb_prod    # Creates the production SQL database"
	@echo "    make migratedb        # Migrates the SQL database"
	@echo "    make migratedb_prod   # Migrates the production SQL database"

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

createdb:
	./manage.py createdb

createdb_prod:
	./manage.py createdb --config_prod

migratedb:
	./manage.py migratedb

migratedb_prod:
	./manage.py migratedb --config_prod



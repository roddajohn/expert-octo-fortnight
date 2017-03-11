setup:
	virtualenv env
	. env/bin/activate
	pip install -r requirements.txt
	export PYTHONPATH='.'

run:
	./manage.py devserver -p 5000

clean:
	rm -r *~

test:	
	py.test app tests

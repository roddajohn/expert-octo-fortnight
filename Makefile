run:
	./manage.py devserver -p 5000

clean:
	rm -r *~

test:	
	py.test --cov-report term-missing --cov app tests

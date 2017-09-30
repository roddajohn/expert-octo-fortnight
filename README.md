# expert-octo-fortnight

[![Build Status](https://travis-ci.org/roddajohn/expert-octo-fortnight.svg?branch=master)](https://travis-ci.org/roddajohn/expert-octo-fortnight)
[![Coverage Status](https://coveralls.io/repos/github/roddajohn/expert-octo-fortnight/badge.svg?branch=master)](https://coveralls.io/github/roddajohn/expert-octo-fortnight?branch=master)

## Work in Progress Disclaimer

<disclaimer>This is a work in progress</disclaimer>

## Installation / Running
Run `make setup` to configure a virutal environment called `env` which will have all the necessary python packages installed.

Prior to running the server, you need to create the database:
`./manage.py createdb` will create a dev database.
`./manage.py --config_prod createdb` will create a production database.

If, at any point in the development, you make a change to the models for the database:
`./manage.py migratedb` will migrate the dev database.
`./manage.py --config_prod migratedb` will migrate the production database.

`./manage.py shell` will run a shell from which you have issue python commands in the virutal env to the database, etc.

To run a development server, run `make run`.  This will output logs to `stdout`.

To run a production server, run `make production`.  This will run a production server.

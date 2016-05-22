# rss-aggregator (c) pubgem

SHELL=/bin/bash
PROJECT_NAME=rss-aggregator
MOD_NAME=rss_aggregator
TEST_CMD=SETTINGS=$$PWD/etc/conf/testing.conf nosetests -w $(MOD_NAME)

install: requirements
	python setup.py install

requirements:
	pip install -r requirements.txt

clean:
	rm -rf build dist *.egg-info
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

server:
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py runserver

shell:
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py shell

aggregate:
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py aggregate

watch:
	watchmedo shell-command -R -p "*.py" -c 'echo \\n\\n\\n\\nSTART; date; $(TEST_CMD) -c etc/nose/test-single.cfg; date' .

test:
	$(TEST_CMD) -c etc/nose/test.cfg

single:
	$(TEST_CMD) -c etc/nose/test-single.cfg

db:
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py init_db
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py populate_db

upgradedb:
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py db upgrade

migratedb:
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py db migrate

apidocs:
	rm -rf var/sphinx/auto-api
	mkdir -p var/sphinx/auto-api/$(MOD_NAME)
	sphinx-apidoc --separate -o var/sphinx/auto-api/$(MOD_NAME) $(MOD_NAME) $(MOD_NAME)/tests
	-rm docs/auto-api
	ln -s $$PWD/var/sphinx/auto-api docs/auto-api

docs:
	rm -rf var/sphinx/build
	SETTINGS=$$PWD/etc/conf/dev.conf sphinx-build -b html docs var/sphinx/build

gh-pages: docs
	rm -rf /tmp/gh-pages
	git clone -b gh-pages git@github.com:pubgem/rss-aggregator.git /tmp/gh-pages
	cp -r var/sphinx/build /tmp/gh-pages
	cd /tmp/gh-pages && git add -A && git commit -am "autosync documentation" && git push -u origin gh-pages

notebook:
	SETTINGS=$$PWD/etc/conf/dev.conf cd var/ipython && ipython notebook

release:
	python setup.py sdist upload -r https://pypi.python.org/pypi

.PHONY: clean install test server watch notebook db single docs shell upgradedb migratedb release requirements apidocs gh-pages aggregate

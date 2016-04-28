rss-aggregator
=============

description

Overview
--------

Flask-Diamond imports many other Flask extensions and glues them all together.  The end result is a model administration view, accounts and high-level account operations (e.g. password reset), testing, documentation, deployment, and more.

Installation
^^^^^^^^^^^^

::

    mkvirtualenv rss-aggregator
    pip install rss-aggregator

Usage
^^^^^

::

    workon rss-aggregator
    diamond-scaffold.sh ~/Documents/new-project
    cd ~/Documents/new-project
    mkvirtualenv -a . new-project

    (install and set-up PostgreSQL w/ username: rss_aggregator, and database pubgem)
    sudo apt-get install postgresql
    sudo su - postgres
    psql -c "CREATE ROLE rss_aggregator PASSWORD 'aaa' NOSUPERUSER NOCREATEDB NOCREATEROLE INHERIT LOGIN"
    psql -c "CREATE DATABASE rss_aggregator OWNER rss_aggregator"

    make install docs test db server

Documentation
^^^^^^^^^^^^^

Libraries
^^^^^^^^^
* `feedparser <https://pythonhosted.org/feedparser/>`_
* Postgresql
* SqlAlchemy + Flask

http://project.pubgem.com

# -*- coding: utf-8 -*-
# rss-aggregator (c) pubgem

import sys
import os
from fabric.api import env, run, open_shell
from fabric.contrib.project import rsync_project

env.user = 'rss-aggregator'
env.key_filename = [os.path.expanduser('~/.ssh/id_rsa')]

if not env.hosts:
    print "need to call with -H [host.example.com]"
    sys.exit(1)


def rsync():
    "rsync local changes (ignoring git)"
    if not os.path.exists("fabfile.py"):
        print "need to run in root of project"
        sys.exit(1)

    excluded = [
        "*.egg-info",
        ".build",
        ".git*",
        "*.pyc",
        "dist",
        "build",
    ]
    rsync_project(remote_dir=env.user, local_dir="./", exclude=excluded, delete=True)


def pull():
    "pull on the remote system"
    run('cd ~/{app} && git pull'.format(app=env.user))


def setup():
    "run python setup.py install, which installs module"
    cmd = 'source ~/.virtualenvs/{app}/bin/activate && cd {app} && make install'
    run(cmd.format(app=env.user))


def ipython():
    "open ipython environment on remote host"
    open_shell("~/.virtualenvs/{app}/bin/shell.py && exit".format(app=env.user))


def shell():
    "open a shell on the remote host"
    open_shell("source ~/.virtualenvs/{app}/bin/activate".format(app=env.user))


def restart():
    "restart app server"
    run("pkill -HUP runserver.py")


def nginx_restart(sudoer="root"):
    "restart nginx"
    env.user = sudoer
    run("sudo killall nginx && sudo /etc/init.d/nginx start")


def logs():
    "watch logs on remote server"
    open_shell("tail -f /var/log/{app}/*log /var/log/nginx/{app}*log && exit".format(app=env.user))


def help():
    "get help on testing and deploying"
    print helpfile

helpfile = """
# quickly copy some changes over
fab rsync setup
"""

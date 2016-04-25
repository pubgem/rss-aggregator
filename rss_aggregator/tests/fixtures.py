# -*- coding: utf-8 -*-
# rss-aggregator (c) pubgem

from .. import models


def typical_workflow():
    "create some example objects"

    a_user = models.User.register(
        email='iandennismiller@gmail.com',
        password='iandennismiller@gmail.com',
        confirmed=True,
        roles=["User"],
    )

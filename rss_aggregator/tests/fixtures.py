# -*- coding: utf-8 -*-
# rss-aggregator (c) pubgem

from ..models import Role, User
from .. import models
import os

MODULE_PATH = os.path.split(os.path.realpath(__file__))[0]


def typical_workflow():
    "create some example objects"

    Role.add_default_roles()
    User.add_guest_user()


def offline_rss_feed():
    "An offline RSS feed as models.RSSFeed model object."
    return models.RSSFeed.find_or_create(
        **{
            "name": "Journal of Personality and Social Psychology",
            "rss_url": os.path.join(MODULE_PATH, "data/psp.rss"),
        }
    )

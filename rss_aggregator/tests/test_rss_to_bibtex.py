# rss-aggregator (c) pubgem

from .. import models
from .. import db
import datetime
from .mixins import DiamondTestCase
from nose.plugins.attrib import attr
from rss_aggregator.rss_to_bibtex import RSSToBibtex


class RSSToBibtexTestCase(DiamondTestCase):
    "Coverage for rss_to_bibtex"

    def setUp(self):
        db.drop_all()
        db.create_all()
        rss_feed = models.RSSFeed.create(**{
            'doi': None,
            'isbn': None,
            'issn': None,
            'name': 'Journal of Personality and Social Psychology',
            'parser_class': 'apa',
            'publisher': None,
            'rss_url': '/home/perlgeist/devel/pubgem/rss-aggregator/rss_aggregator/tests/data/psp.rss',
            'summary': None,
            'www': None})
        models.RSSEntry.create(**{
            'authors': 'Reich, Taly; Wheeler, S. Christian',
            'doi': '10.1037/pspa0000047',
            'date': datetime.datetime.utcnow(),
            'issue': None,
            'pages': None,
            'raw_xml': None,
            'rss_feed': rss_feed,
            'title': 'The good and bad of ambivalence: Desiring ambivalence under outcome uncertainty.',
            'volume': None,
            'www': 'http://feedproxy.google.com/~r/apa-journals-psp/~3/_rhRNeKxYB0/493'})

    @attr('single')
    def test_RSSToBibtex(self):
        "Testing rss_to_bibtex.RSSToBibtex"
        rss_entry = models.RSSEntry.find(doi='10.1037/pspa0000047')
        rss_to_bibtex = RSSToBibtex(rss_entry)
        bibtex = rss_to_bibtex.get_bibtex()
        print(bibtex); assert False;

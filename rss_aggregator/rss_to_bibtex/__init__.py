# rss-aggregator (c) pubgem
import bibtexparser
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bwriter import BibTexWriter
import datetime
import inspect
import sys


class RSSToBibtex:

    def __init__(self, rss_entry):
        self.rss_entry = rss_entry
        self.parser = self.get_parser(rss_entry.rss_feed.parser_class)
        self.bibtex = self.parser(self.rss_entry).get_bibtex()

    @classmethod
    def get_parser(cls, parser_class):
        """
        Dynamically retrieves the parser class based on models.RSSFeed.parser_class

        :param parser_class: models.RSSFeed.parser_class value
        :returns: A relevent Parse class, like Parse_apa, Parse_sage, etc.
        """
        parsers = {k: v for k, v in inspect.getmembers(sys.modules[__name__], inspect.isclass) if "Parse_" in k}
        return parsers["Parse_" + parser_class]

    def __str__(self):
        return self.bibtex

    def get_bibtex(self):
        return self.bibtex


class ParseBase:
    """
    Base Parse class
    """
    def __init__(self, rss_entry):
        self.rss_entry = rss_entry
        self.bib_db = BibDatabase()
        self.parse()

    def parse(self):
        payload = [{
            "ENTRYTYPE": "article",
            "ID": str(),  # First Author Lastname, Year, MD5 hash of title (truncated)
            "doi": self.rss_entry.doi,
            "title": self.rss_entry.title,
            "author": self.rss_entry.authors,  # Determined per Parse_ class
            "journal": self.rss_entry.rss_feed.name,
            "number": self.rss_entry.issue,
            "volume": self.rss_entry.volume,
            "pages": self.rss_entry.pages,
            "year": self.rss_entry.date.year,
            "month": datetime.datetime.strftime(self.rss_entry.date, "%b").lower(),
            # "day": str(self.rss_entry.date.day),
        }]
        self.bib_db.entries = payload

    def get_bibtex(self):
        writer = BibTexWriter()
        return writer.write(self.bib_db)


class Parse_apa(ParseBase):

    pass
    # def parse(self):
    #     super().parse()
    #     payload = {"doi": "yo momma"}
    #     self.bib_db.entries[0].update(payload)


class Parse_sage(ParseBase):
    pass

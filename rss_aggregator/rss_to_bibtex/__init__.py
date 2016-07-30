# rss-aggregator (c) pubgem
import bibtexparser
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bwriter import BibTexWriter
import datetime
import inspect
import hashlib
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
        id = "{author}_{year}_{title}".format(
            author=self.get_authors()[0]["last_name"],
            year=self.rss_entry.date.year,
            title=hashlib.md5(bytes(self.rss_entry.title)).hexdigest()[8:],
        )
        payload = [{
            "ENTRYTYPE": "article",
            "ID": id,  # First Author Lastname, Year, MD5 hash of title (truncated)
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

    def get_authors(self):
        """
        Parses authors field from models.RSSEntry. Usually overridden per parser case
        """
        return self.rss_entry.authors

    def get_bibtex(self):
        writer = BibTexWriter()
        return writer.write(self.bib_db)


class Parse_apa(ParseBase):

    def get_authors(self):
        "Default apa style"
        authors = self.rss_entry.authors.split(";")
        parsed_authors = []
        for i in authors:
            p = i.split(", ")
            author = {
                "last_name": p[0],
                "first_name": p[1].split(". ")[0],
                "middle_names": "".join(p[1].split(". ")[1:]),
            }
            parsed_authors.append(author)
        return parsed_authors


class Parse_sage(ParseBase):
    pass

import pytest

from scraper import search_topic

def test_full_url():
    query = "syndicalism"
    assert query in search_topic(query)
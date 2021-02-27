from anlib import __version__
from anlib.main import get_article


def test_version():
    assert __version__ == '1.1'


def test_check_results_found():
    assert get_article('anarchism') is not None


def test_check_no_results_found():
    assert get_article('jaco') is None

from scraper import get_citations_needed_count, get_citations_needed_report, write_report
from unittest import mock

html = """<html>
<body>
<p>
    Hi This is a test
    <a title="Wikipedia:Citation needed">Citation needed</a>
    Hi This is a test 2
    <a title="Wikipedia:Citation needed">Citation needed</a>
</p>
<p>
    Hi This is a test 3
    <a title="Wikipedia:Citation needed">Citation needed</a>
</p>
</body>
</html>"""


def test_get_citations_needed_count():
    with mock.patch('scraper.requests.get') as mock_get:
        mock_get.return_value.content = html
        assert get_citations_needed_count('mock.url') == 3


def test_get_citations_needed_report():
    with mock.patch('scraper.requests.get') as mock_get:
        mock_get.return_value.content = html
        actual = get_citations_needed_report('mock.url')
        print(actual)
        assert get_citations_needed_report('mock.url') == """
    Hi This is a test
    Citation needed
    Hi This is a test 2
    Citation needed


    Hi This is a test 3
    Citation needed

"""

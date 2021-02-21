import pytest
import requests


@pytest.mark.parametrize('url, status', [
    ('http://127.0.0.1:5000', 200),
    ('http://127.0.0.2:5000', 200),
    ('http://127.0.0.3:5000', 200),
])
def test_connection(url, status):
    assert requests.head(url).status_code == status, f"Check connection {url}"

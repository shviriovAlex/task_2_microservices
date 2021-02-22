import pytest
import requests


@pytest.mark.parametrize('url, status', [
    ('http://localhost:8000', 200),
    ('http://localhost:8001', 200),
    ('http://localhost:8002', 200),
])
def test_connection(url, status):
    assert requests.head(url).status_code == status, f"Check connection {url}"

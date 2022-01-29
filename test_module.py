import pytest
import requests


def test_status_code(base_url, status_code):
    r = requests.get(base_url)
    assert str(r.status_code) == status_code








import pytest
import requests
from jsonschema import validate
import cerberus

url = 'https://jsonplaceholder.typicode.com/'


def test_api_json_schema():
    r = requests.get(url + 'posts/1')

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "userId": {"type": "number"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["id", "userId", "title", "body"]
    }


@pytest.mark.parametrize("url_rout", [
    'posts/1/comments',
    'albums/1/photos',
    'users/1/albums',
    'users/1/todos',
    'users/1/posts',
])
def test_urls_status_code(url_rout):
    r = requests.get(url + url_rout)
    assert r.status_code == 200


@pytest.mark.parametrize("url_rout, count", [
    ('posts/1/comments', 5),
    ('albums/1/photos', 50),
    ('users/1/albums', 10),
    ('users/1/todos', 20),
    ('users/1/posts', 10)
])
def test_count_ids(url_rout, count):
    r = requests.get(url + url_rout)
    assert len(r.json()) == count


@pytest.mark.parametrize("photo", [i for i in range(50)])
def test_photos_availability(photo):
    r = requests.get(url + 'albums/1/photos')
    res_json = r.json()
    image = requests.get(res_json[photo]['url'])
    assert image.status_code == 200


@pytest.mark.parametrize("ids", [i for i in range(10)])
def test_posts_ids(ids):
    r = requests.get(url + 'users/1/posts')
    res_json = r.json()
    id = res_json[ids]['id']
    assert id == ids+1

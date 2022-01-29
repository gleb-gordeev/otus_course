import pytest
import requests
from jsonschema import validate

url = 'https://api.openbrewerydb.org/breweries?'


@pytest.mark.parametrize("filter", ['by_city=san_diego',
                                    'by_dist=38.8977,77.0365',
                                    'by_name=cooper',
                                    'by_state=ohio',
                                    'by_postal=44107',
                                    'by_type=micro',
                                    'page=15',
                                    'per_page=25'
                                    ])
def test_get_status_code_with_filters(filter):
    r = requests.get(url + filter)
    assert r.status_code == 200


def test_status_with_all_filters():
    r = requests.get(url + 'by_city=san_diego' + '&by_dist=38.8977,77.0365' +
                            '&by_name=cooper' + '&by_state=ohio' +
                            '&by_postal=44107' + '&by_type=micro' +
                            '&page=15' + '&per_page=25')
    assert r.status_code == 200


@pytest.mark.parametrize("state", ['Vermont', 'Oregon'])
@pytest.mark.parametrize("type", ['micro', 'closed', 'bar'])
def test_breweries_with_few_filters(state, type):
    r = requests.get(url + 'by_state=' + state + '&by_type=' + type)
    res_json = r.json()
    for i in range(len(res_json)):
        assert res_json[i]['state'] == state
        assert res_json[i]['brewery_type'] == type


@pytest.mark.parametrize("per_page", ['1', '25', '50'])
def test_per_page(per_page):
    r = requests.get(url + 'per_page=' + per_page)
    assert len(r.json()) == int(per_page)


def test_default_per_page():
    r = requests.get(url)
    assert len(r.json()) == 20

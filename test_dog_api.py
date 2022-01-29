import pytest
import requests
import cerberus

url = 'https://dog.ceo/api/'


def test_breed_count():
    res = requests.get(url + 'breeds/list/all')
    res_json = res.json()
    assert len(res_json.get("message")) == 95


@pytest.mark.parametrize("param", [
    'breed/hound/images',
    'breed/hound/images/random',
    'breed/hound/images/random/3',
    'breeds/list/all',
    'breed/hound/list'
    ])
def test_get_status_codes(param):
    r = requests.get(url + param)
    assert r.status_code == 200


@pytest.mark.parametrize("param", ['1', '3', '1000'])
def test_get_multiple_images(param):
    r = requests.get(url + 'breed/hound/images/random/' + param)
    res_json = r.json()
    assert len(res_json.get("message")) == int(param)


def test_api_json_schema():
    res = requests.get(url + 'breed/hound/images/random/')
    schema = {
        "message": {"type": "string"},
        "status": {"type": "string"}
    }

    v = cerberus.Validator()
    assert v.validate(res.json(), schema)


@pytest.mark.parametrize("breeds_with_subreeds", [
    'hound', 'australian', 'buhund', 'bulldog',
    'bullterrier', 'cattledog', 'collie', 'corgi',
    'dane', 'deerhound', 'elkhound', 'finnish',
    'frise', 'greyhound', 'mastiff', 'mountain',
    'ovcharka', 'pinscher', 'pointer', 'poodle',
    'retriever', 'ridgeback', 'schnauzer', 'setter',
    'sheepdog', 'spaniel', 'springer', 'terrier',
    'waterdog', 'wolfhound'
])
def test_sub_breeds(breeds_with_subreeds):
    res = requests.get(url + 'breed/' + breeds_with_subreeds + '/list')
    res_json = res.json()
    assert len(res_json.get("message")) != 0

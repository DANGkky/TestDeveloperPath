from pprint import pprint

import requests


def test_requests():
    r = requests.get("https://ceshiren.com/categories.json")
    pprint(r)
    print(r.status_code)
    print(r.json())
    assert r.status_code == 200


def test_get():
    r = requests.get("https://httpbin.testing-studio.com/get", params={
        "a": 1, "b": 2, "c": "ccc"
    }, headers={"Jacky":"Jacky_demo_test"})
    print(r.json())
    assert r.status_code == 200


def test_post():
    r = requests.post("https://httpbin.testing-studio.com/post", params={"a": 1, "b": 2, "c": "ccc"}, data={
        "a": 111, "b": 222, "c": "cdddcc"
    }, headers={"h": "header demo"})
    print(r.json())
    assert r.status_code == 200
    assert r.json()["headers"]["H"] == "header demo"


def test_upload():
    # url="https://httpbin.testing-studio.com/post"
    url = "https://httpbin.org/post"
    r = requests.post(url,
                      files={"file": open("__init__.py", 'rb')},
                      # headers={"Content-Type": "application/plain"},
                      # cookies={"name": "JackyPinkgin"}
                      )
    print(r.json())
    # print(r.text)
    assert r.status_code == 200


def test_get_wework():
    r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=dhashu&corpsecret=djasduqid1242")
    print(r.json())
    assert r.status_code == 200

import requests
import pytest
class TestDemo:
    @pytest.mark.skip
    def test_get(self):
        r = requests.get('https://baidu.com')
        print(r.status_code)
        print(r.text)
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level": 1,
            "name": "serveniruby"
        }
        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "derveniruby"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        r.status_code == 200

    def test_post_header(self):
        r = requests.get('https://httpbin.testing-studio.com/get', headers={"h": "headerdemo"})
        print(r.text)
        print(r.status_code)
        print(r.json())
        # assert r.status_code == 200
        assert r.json()['headers']["H"] == "headerdemo"

    # def test_post_json(self):
    #     payload = {
    #         "level": 1,
    #         "name": "derveniruby"
    #     }
    #     r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
    #     print(r.text)
    #     # r.status_code == 200
    #     #assert r.json()['json']['level'] == 1

    def test_hogwarts_json(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == '霍格沃兹测试学院公众号'


import pytest
import requests

datas = [
    {"password": "123456", "userName": "jack", "expect": [200, "登录成功", "10000"]},
    {"password": "12345", "userName": "jack", "expect": [200, "登录失败", "1002"]}
]

@pytest.fixture(params=datas)
def login_fixture(request):
    print("数据库查验账号, 用户名：%s, 密码：%s" % (request.param["userName"], request.param["password"]))
    yield request.param
    print("登录测试用例结束")

class TestCaseLogin:

    def test001(self, login_fixture):
        data = {"userName": login_fixture["userName"], "password": login_fixture["password"]}
        r = requests.post("http://www.ndtester.com:8084/loginApi", data=data)
        json = r.json()
        assert login_fixture["expect"][0] == r.status_code
        assert login_fixture["expect"][1] in json["message"]
        assert login_fixture["expect"][2] == json["code"]



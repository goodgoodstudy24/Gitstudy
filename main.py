import pytest
from time import strftime

if __name__ == "__main__":
    # pytest.main() # 默认查找当前目录下，符合编写规则的测试用例
    # pytest.main(["requests_day2.py"]) # 指定运行的测试文件
    # pytest.main(["-s", "requests_day2.py"]) # -s表示显示测试用例中print的输出内容
    # pytest.main(["-v", "requests_day2.py"]) # -v显示详细信息
    # pytest.main(["-v", "-s","requests_day2.py"]) # 显示详细信息和输出内容
    # pytest.main(["-vs", "requests_day2.py"]) # 显示详细信息和输出内容，同上一个
    # pytest.main(["-q", "requests_day2.py"]) # 不显示环境信息
    # pytest.main(["requests_day2.py::LoginTestCase::test001"]) # 指定执行某个类中的测试用例
    # -k 关键字，表示只运行带有关键字的测试用例
    # pytest.main(["-v", "-k", "1", "requests_day2.py"])
    # --lf: 表示执行上一次运行失败的用例，如果上一次没有失败的用例则执行所有用例
    # pytest.main(["-v", "--lf", "requests_day2.py"])
    # pytest.main(["-vs",'mark_skip.py'])
    # pytest.main(["-vs", "login_test.py::test003"]) # 运行指定的测试用例（函数）
    # pytest.main(["-vs", "setup_teardown.py"]) # 按照模块中的编写顺序执行
    # pytest.main(["-vs", "fixture_autouse_test.py"])
    # pytest.main(["-vs", "params.py"])
    # pytest.main(["-vs", "login_params_test.py"])
    # pytest.main(["-vs", "mark_skip.py"])
    # pytest.main(["-vs", "mark_order.py"])
    # -m 标签名: 指定运行该标签装饰的测试用例
    # pytest.main(["-vs", "-m", "smoke", "marker_conf.py"]) # 只运行被pytest.mark.smoke装饰的测试用例
    # pytest.main(["-vs", "-m smoke", "marker_conf.py"])
    # pytest.main(["-vs", "-m test or smoke", "marker_conf.py"]) # 运行被smoke或者test装饰的测试用例
    # pytest.main(["-vs", "-m", "not test and not smoke", "marker_conf.py"]) # 运行非test和smoke装饰的测试用例
    # pytest.main(["-vs", "-m", "test_smoke or test_order", "marker_conf.py"])
    pytest.main(['--html=./report%s.html'%strftime('%y-%m-%d'),'marker_conf.py'])
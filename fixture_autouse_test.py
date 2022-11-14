import pytest

# autouse参数: 表示fixture函数自动运行
# 默认scope="function"，设置scope后，按照范围从大到小的顺序执行
@pytest.fixture(autouse=True)
def fixture_function():
    print("测试用例执行前")
    yield
    print("测试用例执行后")

@pytest.fixture(autouse=True, scope="class")
def fixture_class():
    print("测试类执行前")
    yield
    print("测试类执行后")

@pytest.fixture(autouse=True, scope="module")
def fixture_module():
    print("模块中的所有测试用例执行前")
    yield
    print("模块中的所有测试用例执行后")

@pytest.fixture(autouse=True, scope="package")
def fixture_package():
    print("包中的所有测试用例执行前")
    yield
    print("包中的所有测试用例执行后")

@pytest.fixture(autouse=True, scope="session")
def fixture_session():
    print("每一个session的所有测试用例执行前")
    yield
    print("每一个session中的所有测试用例执行后")

def test001():
    print("test001")

def test002():
    print("test002")

class TestA:

    def test003(self):
        print("test003")

    def test004(self):
        print("test004")


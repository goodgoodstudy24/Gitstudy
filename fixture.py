import pytest

# 装饰器是固定的格式
@pytest.fixture()
def fixture_function(): # fixture函数名称没有要求
    print("测试用例运行前执行")
    yield # 固定写法，yield前的代码为前置步骤，yield后的代码为后置步骤
    print("测试用例运行后执行")

@pytest.fixture
def fixture1():
    print("测试用例前步骤一")

@pytest.fixture()
def fixture2():
    yield
    print("测试用例后步骤二")



def test001(fixture1):
    print("test001")

# 方式一：将fixture函数作为参数传递后，来调用
def test002(fixture_function):
    print("test002")

@pytest.mark.usefixtures("fixture1")
@pytest.mark.usefixtures("fixture2")
def test007():
    print("test007")

def test005(fixture2):
    print("test005")

def test006(fixture1, fixture2):
    print("test006")

class TestA:

    # 方式二：将fixture函数作为值传入装饰器中（装饰器为固定格式）
    @pytest.mark.usefixtures("fixture_function")
    def test003(self):
        print("test003")

    def test004(self, fixture_function):
        print("test004")
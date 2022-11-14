import pytest

def setup_module():
    """模块中所有测试用例执行前运行一次"""
    print("setup module")

def teardown_module():
    """模块中所有测试用例执行后运行一次"""
    print("teardown module")

def setup_function():
    """每一个测试函数（不在类里的函数）执行前运行一次"""
    print("setup function")

def teardown_function():
    """每一个测试函数（不在类里的函数）执行后运行一次"""
    print("teardown function")

class TestA:

    def setup_class(self):
        """测试类中的所有测试方法执行前只运行一次"""
        print("setup class")

    def teardown_class(self):
        """测试类中的所有测试方法执行后只运行一次"""
        print("teardown class")

    def setup_method(self):
        """测试类中的所有测试方法执行前都要运行一次"""
        print("setup method")

    def teardown_method(self):
        """测试类中的所有测试方法执行后都要运行一次"""
        print("teardown method")

    def test003(self):
        print("test003")

    def test004(self):
        print("test004")

def test001():
    print("test001")

def test002():
    print("test002")
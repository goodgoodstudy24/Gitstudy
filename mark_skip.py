import pytest

@pytest.mark.skip
def test001():
    print("test001")

def test002():
    print("test002")

@pytest.mark.skip(reason="测试skip跳过此用例")
def test003():
    print("test003")

# skipif，条件为True，跳过此用例；反之，则运行。reason只在跳过的测试用例显示
@pytest.mark.skipif(1 == 1, reason="True, 测试skipif跳过此用例")
def test004():
    print("test004")

@pytest.mark.skipif(2 == 1, reason="False, 测试skipif没有跳过此用例")
def test005():
    print("test005")

# 用例通过显示XPASS, 用例失败显示XFAIL；使用场景：已知用例为阻塞状态，不管成功与否都不在意它的结果
# 如果xfail设置了条件，条件为True, 则将测试用例显示为XPASS或XFAIL；反之，则显示为PASSED或FAILED
@pytest.mark.xfail()
def test006():
    print("test006")

@pytest.mark.xfail(reason="测试xfail的功能")
def test007():
    print("test007")
    assert "a" in "bcd"

@pytest.mark.xfail(1 == 1, reason="True, 测试xfail的功能")
def test008():
    print("test008")

@pytest.mark.xfail(2 == 1, reason="False, 测试xfail的功能")
def test009():
    print("test009")
    assert "a" in "bcd"
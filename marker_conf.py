import pytest

@pytest.mark.smoke
def test001():
    print("test001")

@pytest.mark.test
def test002():
    print("test002")

@pytest.mark.test_smoke
def test003():
    print("test003")

@pytest.mark.test_order
def test004():
    print("test004")
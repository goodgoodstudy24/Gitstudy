import pytest


@pytest.mark.order(after="test001")
def test006():
    print("test006")

def test001():
    print("test001")

@pytest.mark.order(-1)
def test002():
    print("test002")

def test003():
    print("test003")

@pytest.mark.order(0)
def test004():
    print("test004")

@pytest.mark.order(before="test001")
def test005():
    print("test005")

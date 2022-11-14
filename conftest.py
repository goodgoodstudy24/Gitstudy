import pytest

def pytest_configure(config):
    config.addinivalue_line("markers", "test_smoke: smoking test")
    config.addinivalue_line("markers", "test_order: testing")


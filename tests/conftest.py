import copy
import pytest

from fastapi.testclient import TestClient

import src.app as app_module

# keep an immutable snapshot of the "database" so we can restore it
_original_activities = copy.deepcopy(app_module.activities)


@pytest.fixture
def client():
    """Yields a TestClient instance for the FastAPI app."""
    with TestClient(app_module.app) as client:
        yield client


@pytest.fixture(autouse=True)
def reset_activities():
    """Autouse fixture that restores the in-memory activities before each test."""
    # Arrange (fixture setup)
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(_original_activities))
    yield
    # no teardown necessary – each test gets a fresh copy anyway

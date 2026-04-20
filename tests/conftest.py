import pytest
from copy import deepcopy
from fastapi.testclient import TestClient
from src.app import app, activities


# Store original activities state for restoration
_ORIGINAL_ACTIVITIES = deepcopy(activities)


@pytest.fixture
def client():
    """Provide TestClient for testing FastAPI app"""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """
    Automatically reset in-memory activities to initial state before each test.
    This prevents cross-test contamination from signup/unregister mutations.
    """
    # Restore to original state before test runs
    activities.clear()
    activities.update(deepcopy(_ORIGINAL_ACTIVITIES))
    yield
    # Cleanup after test (optional, but good practice)
    activities.clear()
    activities.update(deepcopy(_ORIGINAL_ACTIVITIES))

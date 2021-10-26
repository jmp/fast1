from _pytest.fixtures import fixture
from starlette.testclient import TestClient

from app.main import app


@fixture(scope="session")
def client() -> TestClient:
    return TestClient(app)

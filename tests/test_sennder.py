import requests
import pytest
from ..ghibil.app import api


@pytest.fixture
def client(request):
    test_client = api.test_client()
    return test_client


def test_films(client):
    response = client.get("/films/")
    assert response.data is not None

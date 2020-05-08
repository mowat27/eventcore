import os
import tempfile

import pytest

from eventcore import api


@pytest.fixture
def client():
    api.app.config['TESTING'] = True
    with api.app.test_client() as client:
        yield client


def test_index(client):
    assert client.get("/").data == b'{"items": []}'

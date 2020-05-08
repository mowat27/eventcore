import os

import boto3
import pytest
from moto import mock_dynamodb2

os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
os.environ['AWS_SECURITY_TOKEN'] = 'testing'
os.environ['AWS_SESSION_TOKEN'] = 'testing'


@pytest.fixture
def ddb(scope='function'):
    with mock_dynamodb2():
        return boto3.client('dynamodb')

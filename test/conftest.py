import pytest

import boto3
from moto import mock_dynamodb2


@pytest.fixture
def ddb(scope='function'):
    with mock_dynamodb2():
        return boto3.client('dynamodb',
                            region_name='eu-west-1',
                            aws_access_key_id='testing',
                            aws_secret_access_key='testing',
                            aws_session_token='testing')

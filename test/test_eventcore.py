import os
from uuid import uuid4
import pytest
from moto import mock_dynamodb2


os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
os.environ['AWS_SECURITY_TOKEN'] = 'testing'
os.environ['AWS_SESSION_TOKEN'] = 'testing'


def create_events_table(ddb):
    table_name = 'Events-{}'.format(str(uuid4()))
    ddb.create_table(
        TableName=table_name,
        AttributeDefinitions=[
            {
                'AttributeName': 'eventId',
                'AttributeType': 'S',
            }
        ],
        KeySchema=[
            {
                'AttributeName': 'eventId',
                'KeyType': 'HASH',
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1,
        }
    )
    return table_name


def create_streams_table(ddb):
    table_name = 'Streams-{}'.format(str(uuid4()))
    ddb.create_table(
        TableName=table_name,
        AttributeDefinitions=[
            {
                'AttributeName': 'streamId',
                'AttributeType': 'S'
            }
        ],
        KeySchema=[
            {
                'AttributeName': 'streamId',
                'KeyType': 'HASH'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1,
        }
    )
    return table_name


@mock_dynamodb2
def test_stream_not_found(ddb):
    # Prefer local imports to ensure mocks are setup already
    from eventcore.eventcore import EventCore

    eventcore = EventCore(ddb,
                          streams_table=create_streams_table(ddb),
                          events_table=create_events_table(ddb))
    assert eventcore.stream_exists("user-1") is False


@mock_dynamodb2
def test_stream_creation(ddb):
    # Prefer local imports to ensure mocks are setup already
    from eventcore.eventcore import EventCore

    eventcore = EventCore(ddb,
                          streams_table=create_streams_table(ddb),
                          events_table=create_events_table(ddb))
    eventcore.create_stream("user-1")
    assert eventcore.stream_exists("user-1") is True

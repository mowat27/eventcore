class EventCore:
    def __init__(self, client, streams_table, events_table):
        self._client = client
        self._streams_table = streams_table
        self._events_table = events_table

    def stream_exists(self, stream_id):
        response = self._client.get_item(
            TableName=self._streams_table,
            Key={
                "streamId": {"S": stream_id}
            }
        )
        return "Item" in response

    def create_stream(self, stream_id):
        self._client.put_item(
            TableName=self._streams_table,
            Item={
                "streamId": {"S": stream_id}
            }
        )

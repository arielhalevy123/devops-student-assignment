import pytest
from lambda_code import handler

def test_list_s3_files_empty(monkeypatch):
    """Test list_s3_files returns empty list when no files exist."""

    class MockS3Client:
        def list_objects_v2(self, Bucket):
            return {}

    monkeypatch.setattr(handler.boto3, "client", lambda service: MockS3Client())
    files = handler.list_s3_files("fake-bucket")
    assert files == []

def test_list_s3_files_with_objects(monkeypatch):
    """Test list_s3_files returns correct file names."""

    class MockS3Client:
        def list_objects_v2(self, Bucket):
            return {
                "Contents": [{"Key": "file1.txt"}, {"Key": "file2.txt"}]
            }

    monkeypatch.setattr(handler.boto3, "client", lambda service: MockS3Client())
    files = handler.list_s3_files("fake-bucket")
    assert files == ["file1.txt", "file2.txt"]

def test_send_sns_message(monkeypatch):
    """Test send_sns_message sends correct message."""

    called = {}

    class MockSNSClient:
        def publish(self, TopicArn, Message):
            called["TopicArn"] = TopicArn
            called["Message"] = Message
            return {}

    monkeypatch.setattr(handler.boto3, "client", lambda service: MockSNSClient())
    handler.send_sns_message("fake-topic", "test message")

    assert called["TopicArn"] == "fake-topic"
    assert called["Message"] == "test message"
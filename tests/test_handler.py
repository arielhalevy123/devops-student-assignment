import pytest
from lambda_code import handler

def test_list_s3_files_empty(monkeypatch):
    """Check that the function returns an empty list when no files exist"""

    class MockS3Client:
        def list_objects_v2(self, Bucket):
            return {}

    monkeypatch.setattr(handler, "s3", MockS3Client())
    files = handler.list_s3_files("fake-bucket")
    assert files == []

def test_list_s3_files_with_objects(monkeypatch):
    """Check that the function returns correct file names"""

    class MockS3Client:
        def list_objects_v2(self, Bucket):
            return {
                "Contents": [{"Key": "file1.txt"}, {"Key": "file2.txt"}]
            }

    monkeypatch.setattr(handler, "s3", MockS3Client())
    files = handler.list_s3_files("fake-bucket")
    assert files == ["file1.txt", "file2.txt"]

def test_send_sns_message(monkeypatch):
    """Check that the function sends the message correctly"""
    called = {}

    class MockSNSClient:
        def publish(self, TopicArn, Message):
            called["TopicArn"] = TopicArn
            called["Message"] = Message
            return {}

    monkeypatch.setattr(handler, "sns", MockSNSClient())
    handler.send_sns_message("fake-topic", "test message")

    assert called["TopicArn"] == "fake-topic"
    assert called["Message"] == "test message"
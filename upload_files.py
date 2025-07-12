import boto3
import os


bucket_name = "niceassignmentstack-niceassignmentbucketc5e5d7f2-eropzioganqq"


s3 = boto3.client("s3")


folder_path = "sample_files"


for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        print(f"Uploading {filename}...")
        s3.upload_file(file_path, bucket_name, filename)

print("✅ All files uploaded successfully!")
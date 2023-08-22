import pytest
from moto import mock_s3
import boto3
import os
from upload_to_s3 import upload_code_to_s3
from download_from_s3 import download_code_from_s3
import tarfile

BUCKET_NAME = 'my-artifact-bucket'
FILE_NAME = 'code.tar.gz'


@pytest.fixture
def aws_credentials() -> None:
    """Mocked AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'


@pytest.fixture
def s3(aws_credentials) -> boto3.resource:
    """Set up S3 resource with mocked S3 bucket."""
    with mock_s3():
        conn = boto3.resource('s3', region_name='us-east-1')
        conn.create_bucket(Bucket=BUCKET_NAME)
        yield conn


def test_upload_and_download(s3: boto3.resource) -> None:
    """
    Test the upload and download functions for S3.

    :param s3: Mocked S3 resource.
    """
    # Create a sample file to be included in the tar.gz
    with open('sample_file.txt', 'w') as file:
        file.write('Sample content')

    # Upload the code to S3
    upload_code_to_s3(BUCKET_NAME, FILE_NAME)

    # Verify that the file was uploaded to S3
    s3_client = boto3.client('s3')
    response = s3_client.list_objects(Bucket=BUCKET_NAME)
    assert 'Contents' in response, "File not found in S3 bucket"
    assert response['Contents'][0]['Key'] == FILE_NAME, "File name mismatch in S3 bucket"

    # Download the code from S3
    download_code_from_s3(BUCKET_NAME, FILE_NAME)

    # Verify that the file was downloaded and extracted correctly
    assert os.path.exists(FILE_NAME), "Downloaded file not found"
    with tarfile.open(FILE_NAME, 'r:gz') as tar:
        tar.extractall('extracted_code')
    assert os.path.exists('extracted_code/sample_file.txt'), "Extracted file not found"
    with open('extracted_code/sample_file.txt', 'r') as file:
        content = file.read()
    assert content == 'Sample content', "Content mismatch in extracted file"

    # Clean up
    os.remove('sample_file.txt')
    os.remove(FILE_NAME)
    os.rmdir('extracted_code')

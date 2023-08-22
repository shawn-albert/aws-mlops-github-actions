import boto3
import tarfile

def download_code_from_s3(bucket_name: str, file_name: str = 'code.tar.gz') -> None:
    """
    Downloads a tar.gz file from an S3 bucket and extracts it.

    :param bucket_name: Name of the S3 bucket to download from.
    :param file_name: Name of the tar.gz file to download and extract.
    """
    # Download from S3
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, file_name, file_name)

    # Extract the tar.gz file
    with tarfile.open(file_name, 'r:gz') as tar:
        tar.extractall()

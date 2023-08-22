import boto3
import tarfile
import os

def upload_code_to_s3(bucket_name: str, file_name: str = 'code.tar.gz') -> None:
    """
    Compresses the current directory and uploads it to an S3 bucket.

    :param bucket_name: Name of the S3 bucket to upload to.
    :param file_name: Name of the tar.gz file to create and upload.
    """
    # Create a tar.gz file
    with tarfile.open(file_name, 'w:gz') as tar:
        tar.add('.', arcname=os.path.basename('.'))
    
    # Upload to S3
    s3 = boto3.client('s3')
    s3.upload_file(file_name, bucket_name, file_name)

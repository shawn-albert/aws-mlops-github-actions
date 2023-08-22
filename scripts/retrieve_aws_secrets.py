import boto3
import os

def retrieve_aws_secrets_and_parameters() -> None:
    """Retrieve secrets and parameters from AWS Systems Manager Parameter Store and set as environment variables."""
    ssm = boto3.client('ssm')

    parameters = {
        "GITHUB-TOKEN": "/path/to/github_token",
        "AWS-REGION": "/path/to/aws_region",
        "ECR-REPOSITORY-MAIN": "/path/to/ecr_repository_main",
        "ECR-REPOSITORY-DEVELOP": "/path/to/ecr_repository_develop",
        "ARTIFACT-BUCKET": "/path/to/artifact_bucket",
        "SAGEMAKER-PROJECT-ID": "/path/to/sagemaker_project_id"
    }

    for key, path in parameters.items():
        value = ssm.get_parameter(Name=path, WithDecryption=True)['Parameter']['Value']
        os.environ[key] = value

    # Assuming the SageMaker project name is derived from the GitHub repository name
    os.environ["SAGEMAKER-PROJECT-NAME"] = os.environ['GITHUB_REPOSITORY'].split('/')[-1]

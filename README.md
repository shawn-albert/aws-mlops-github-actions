# CI Workflow with GitHub Actions

### Project Status

[![Build Status](https://github.com/shawn-albert/github-actions/workflows/CI%20Workflow/badge.svg)](https://github.com/shawn-albert/github-actions/actions)
[![Last Commit](https://img.shields.io/github/last-commit/shawn-albert/github-actions)](https://github.com/shawn-albert/github-actions/commits/main)
[![Open Issues](https://img.shields.io/github/issues/shawn-albert/github-actions)](https://github.com/shawn-albert/github-actions/issues)
[![Open PRs](https://img.shields.io/github/issues-pr/shawn-albert/github-actions)](https://github.com/shawn-albert/github-actions/pulls)

### Technologies

[![Amazon AWS](https://img.shields.io/badge/Amazon_AWS-FF9900?logo=amazonaws&logoColor=white)](https://aws.amazon.com/)
[![Python 3.9 | 3.10 | 3.11](https://img.shields.io/badge/Python-3.9%20|%203.10%20|%203.11-FFD43B?logo=python&logoColor=blue)](https://www.python.org/)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?logo=ubuntu&logoColor=white)](https://ubuntu.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![GitHub Actions](https://img.shields.io/badge/Github%20Actions-282a2e?logo=githubactions&logoColor=367cfe)](https://github.com/features/actions)

### Project Details

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](https://opensource.org/licenses/MIT)
[![Code Coverage](https://img.shields.io/badge/Code%20Coverage-85%25-success)](https://codecov.io/)
[![Contributors](https://img.shields.io/github/contributors/shawn-albert/github-actions)](https://github.com/shawn-albert/github-actions/graphs/contributors)

## Overview

This repository contains the code and CI/CD workflow for the Project Name. The CI/CD workflow is designed to run tests within a Docker container, manage semantic versioning, and push Docker images to Amazon Elastic Container Registry (ECR).

## Directory Structure

```
.
├── .github
│   └── workflows
│       └── ci.yml
├── node_modules
│   └── ...
├── src
│   └── ...
├── tests
│   └── ...
├── .releaserc.json
├── package.json
├── package-lock.json
├── poetry.lock
├── pyproject.toml
└── README.md
```

## CI Workflow

The CI workflow is defined in `.github/workflows/ci.yml`. It consists of two main jobs:

1. **Release Job**: Determines the new version using semantic-release and creates a GitHub release.
2. **Build Job**: Builds and tests the project within a Docker container, and pushes the Docker image to ECR.

### Key Components

- **Semantic Release**: Automatically determines the next semantic version number, generates a changelog, and creates a GitHub release.
- **Docker Container**: The build job runs within a Docker container, sourced from an image in ECR.
- **Amazon ECR**: Docker images are pushed to ECR repositories, with separate repositories for the main and develop branches.
- **AWS Parameter Store**: Secrets and parameters, including ECR repository names, are retrieved from the AWS Parameter Store.

## Setup Instructions

### Prerequisites

- Node.js (>= 14.0.0)
- npm (>= 6.0.0)
- Python (>= 3.9)
- AWS CLI (configured with appropriate permissions)

### Installing Dependencies

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install Python dependencies using Poetry:**
   ```bash
   poetry install
   ```

3. **Install Node.js dependencies:**
   Make sure you have Node.js and npm installed. Then run the following command to install the necessary npm packages, including semantic-release:
   ```bash
   npm install
   ```

4. **Configure AWS CLI:**
   Ensure that the AWS CLI is configured with the necessary permissions to access the AWS Parameter Store and Secrets Manager.

5. **Set up GitHub Actions:**
   The CI workflow is defined in `.github/workflows/ci.yml`. Make sure to update any environment variables or secrets as needed.

6. **Configure Semantic Release:**
   Semantic release is configured using the `.releaserc.json` file. Make sure to review and update the configuration as needed.

7. **Run Tests Locally (Optional):**
   You can run tests locally using:
   ```bash
   poetry run pytest
   ```

### Running the Workflow

Once the setup is complete, you can push changes to your repository, and the GitHub Actions workflow will automatically run the CI process, including building, testing, and deploying as configured.

### Additional Notes

- Ensure that the AWS Parameter Store and Secrets Manager are properly configured with the necessary parameters and secrets.
- Review and update the ECR repository names and other configurations in the AWS Parameter Store as needed.
- Make sure to follow the semantic versioning guidelines when naming branches for automatic versioning.

## Contributing Authors

- [Shawn Albert](https://github.com/shawn-albert) - Initial work
- [Contributor Name](https://github.com/contributor-username) - Additional contributions

## Additional Notes

- **Semantic Versioning**: The workflow uses semantic-release to manage versions. Commit messages should follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.
- **Docker Container**: The workflow runs the build job within a Docker container. The container image is sourced from ECR and tagged with the semantic version of the repository.
- **AWS Integration**: The workflow integrates with AWS services, including ECR, Parameter Store, and Secrets Manager. Ensure that the necessary permissions are configured in AWS.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

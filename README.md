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

This repository contains a continuous integration (CI) workflow using GitHub Actions. The workflow checks out the code, sets up a Python environment with poetry, runs tests, builds a Docker container, and saves the container to Amazon ECS.

## Directory Structure

```
.
├── .github
│   └── workflows
│       └── ci.yml
├── Dockerfile
├── task-definition.json
├── pyproject.toml
└── README.md
```

## Step-by-Step Instructions

1. **Set Up the Repository**: Clone this repository and navigate to the project directory.
2. **Configure AWS CLI**: Ensure that the AWS CLI is configured on your self-hosted runners with the necessary IAM roles and permissions to interact with ECS.
3. **Install Poetry**: Ensure that poetry is installed on your self-hosted runners.
4. **Verify Python Versions**: Ensure that the Python versions (3.9, 3.10, 3.11) are available on your self-hosted runners.
5. **Build and Test Locally**: Before pushing to the repository, you can build and test the Docker container locally:
   ```
   docker build -t my-container:latest .
   docker run my-container:latest
   ```
6. **Push Changes**: Commit and push your changes to the `main` branch. The GitHub Actions workflow will be triggered automatically.
7. **Monitor the Workflow**: You can monitor the progress of the workflow in the "Actions" tab of your GitHub repository.
8. **Verify in ECS**: Verify that the Docker container has been saved and the service has been created in your ECS cluster.

## Contributing Authors

- [Shawn Albert](https://github.com/shawn-albert) - Initial work
- [Contributor Name](https://github.com/contributor-username) - Additional contributions

## Additional Notes

- Customize the `Dockerfile`, `task-definition.json`, and `pyproject.toml` as needed for your specific project.
- Add any additional build, test, or deployment steps to the workflow as needed.
- Replace the badges with the correct URLs for your repository.
- Add contributing authors as needed.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

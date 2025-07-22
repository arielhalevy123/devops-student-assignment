# Nice Assignment

## Overview

This project is a fully automated serverless application deployed on AWS using Infrastructure as Code (IaC) with AWS CDK (Python).

The application performs the following:
- Lists all objects in an S3 bucket.
- Sends an email notification with execution details using SNS.
- Uploads sample files to the S3 bucket during deployment.
- Supports manual triggering of the Lambda function for testing.

---

## Setup & Deployment

### Prerequisites
- AWS account with programmatic access
- Python 3.11
- Node.js (for CDK)
- AWS CDK installed
- GitHub account

### Clone the repository
```bash
git clone https://github.com/arielhalevy123/nice-assignment.git
cd nice-assignment
```

### Install dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
npm install -g aws-cdk
```

### Configure AWS credentials
```bash
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=eu-central-1
```

### Deploy
```bash
cdk deploy --require-approval never
```

---

## GitHub Actions

This repository includes GitHub Actions workflows under `.github/workflows/`:

- **deploy.yml**: Installs dependencies, runs tests, deploys the CDK stack, and uploads sample files to S3 automatically.
- **upload_files.yml** (optional): Uploads files to the S3 bucket separately if needed.
- **Tests are run automatically on each push or pull request to ensure code quality and verify infrastructure.**

### Tests include

- Unit tests for the Lambda function logic (using `pytest` and `monkeypatch`).
- Infrastructure tests to verify resources created by CDK (using `aws_cdk.assertions`).

---

## Lambda Function Details

- Language: Python 3.11
- Functionality:
  - Lists objects in the S3 bucket
  - Publishes an SNS message with the list of files
- IAM permissions:
  - S3 read access
  - SNS publish access
  - Lambda execution role

---

## S3 Bucket

- Created via CDK
- Files from `sample_files/` can be uploaded manually via `upload_files.py` or using a dedicated workflow

---

## SNS & Email Subscription

- An SNS topic is created via code
- You will receive an email upon Lambda execution  
**Important:** Make sure to confirm your email subscription after the first deployment (check your email for the confirmation link)

---

## Manual Lambda Test

You can manually invoke the Lambda function from the AWS Console:

1. Go to AWS Lambda Console → Your function → Test
2. Create a new test event (you can keep the default content)
3. Click **Test** and check CloudWatch logs and your email for results

### Manual Lambda Invocation via CLI

You can also invoke the Lambda function locally using the provided script:

```bash
python invoke_lambda.py
```

> This script uses `boto3` and requires your AWS credentials and region to be configured.

---

## Tools & Frameworks Used

- AWS CDK (Python)
- AWS Lambda
- AWS S3
- AWS SNS
- GitHub Actions
- Boto3 (for file upload script)

---

## Folder Structure

```
nice-assignment/
├── .github/
│   └── workflows/
│       ├── deploy.yml
│       └── upload_files.yml  (optional)
├── lambda_code/
│   └── handler.py
├── nice_assignment_stack/
│   ├── __init__.py
│   └── nice_assignment_stack.py
├── sample_files/
│   ├── file1.txt
│   ├── file2.txt
│   ├── file3.txt
│   └── file4.txt
├── tests/
│   ├── __init__.py
│   ├── test_handler.py
│   └── unit/
│       └── test_stack_creates_expected_resources.py
├── upload_files.py
├── invoke_lambda.py
├── app.py
├── cdk.json
├── requirements.txt
├── requirements-dev.txt
├── README.md
└── .gitignore
```

---

## Status

- Fully deployed
- Email notifications working
- Files uploaded
- Manual and automated triggers tested

---

## Contact

For any questions, feel free to open an issue or contact me directly via GitHub.
"""

# Write to a file
with open("/mnt/data/README_final.md", "w") as f:
    f.write(readme_content)

"/mnt/data/README_final.md"

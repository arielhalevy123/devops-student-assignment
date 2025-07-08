# DevOps Student Assignment

## 🌟 Overview

This project is a fully automated serverless application deployed on AWS using Infrastructure as Code (IaC) with AWS CDK (Python).

The application performs the following:
- Lists all objects in an S3 bucket.
- Sends an email notification with execution details using SNS.
- Uploads sample files to the S3 bucket during deployment.
- Supports manual triggering of the Lambda function for testing.

---

## 🚀 Setup & Deployment

### Prerequisites
- AWS account with programmatic access.
- Python 3.9
- Node.js (for CDK)
- AWS CDK installed (`npm install -g aws-cdk`)
- GitHub account

### Clone the repository
```bash
git clone https://github.com/arielhalevy123/devops-student-assignment.git
cd devops-student-assignment
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

## 💻 GitHub Actions

A GitHub Actions workflow (`.github/workflows/deploy.yml`) is configured to:
- Deploy the CDK stack.
- Upload files from `sample_files/` to S3.
- Trigger manually using `workflow_dispatch`.

---

## 📄 Lambda Function Details

- Language: Python 3.9
- Functionality:
  - Lists objects in the S3 bucket.
  - Publishes an SNS message with the list of files.
- IAM permissions:
  - S3 read access
  - SNS publish access
  - Lambda execution role

---

## ☁️ S3 Bucket

- Created via CDK.
- Files from `sample_files/` are uploaded automatically as part of deployment.

---

## ✉️ SNS & Email Subscription

- An SNS topic is created via code.
- You will receive an email upon Lambda execution.  
⚠️ **Important:** Make sure to confirm your email subscription after the first deployment (check your email for the confirmation link).

---

## 🧪 Manual Lambda Test

You can manually invoke the Lambda function from the AWS Console:

1️⃣ Go to AWS Lambda Console → Your function → Test.  
2️⃣ Create a new test event (you can keep the default content).  
3️⃣ Click **Test** and check CloudWatch logs and your email for results.

---

## ⚙️ Tools & Frameworks Used

- AWS CDK (Python)
- AWS Lambda
- AWS S3
- AWS SNS
- GitHub Actions
- Boto3 (for file upload script)

---

## 📂 Folder Structure

```
devops-student-assignment/
├── .github/workflows/
│   └── deploy.yml
├── devops_student_assignment/
│   ├── __init__.py
│   └── devops_student_assignment_stack.py
├── sample_files/
│   ├── file1.txt
│   └── file2.txt
├── upload_files.py
├── app.py
├── cdk.json
├── requirements.txt
├── README.md
```

---

## ✅ Status

- ✅ Fully deployed
- ✅ Email notifications working
- ✅ Files uploaded
- ✅ Manual and automated triggers tested

---

## 💬 Contact

For any questions, feel free to open an issue or contact me directly via GitHub.

---

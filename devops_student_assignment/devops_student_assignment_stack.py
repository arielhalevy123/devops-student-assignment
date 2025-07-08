from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    RemovalPolicy
)
from constructs import Construct
import os

class DevopsStudentAssignmentStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # S3 Bucket
        bucket = s3.Bucket(self,
                           "MyBucket",
                           versioned=True,
                           removal_policy=RemovalPolicy.DESTROY,
                           auto_delete_objects=True)

        # SNS Topic
        topic = sns.Topic(self, "MyTopic")
        topic.add_subscription(subs.EmailSubscription("ariel67788@icloud.com")) 

        # IAM Role
        lambda_role = iam.Role(self, "MyLambdaRole",
                               assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"))
        lambda_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole"))
        lambda_role.add_to_policy(iam.PolicyStatement(
            actions=["s3:ListBucket", "sns:Publish"],
            resources=["*"]
        ))

        # Lambda Function
        function = _lambda.Function(self, "MyFunction",
                                    runtime=_lambda.Runtime.PYTHON_3_9,
                                    handler="index.handler",
                                    role=lambda_role,
                                    code=_lambda.Code.from_inline(
                                        "import boto3\n"
                                        "import os\n"
                                        "\n"
                                        "s3 = boto3.client('s3')\n"
                                        "sns = boto3.client('sns')\n"
                                        "\n"
                                        "def handler(event, context):\n"
                                        "    bucket_name = os.environ['BUCKET_NAME']\n"
                                        "    topic_arn = os.environ['TOPIC_ARN']\n"
                                        "    response = s3.list_objects_v2(Bucket=bucket_name)\n"
                                        "    files = [obj['Key'] for obj in response.get('Contents', [])]\n"
                                        "    message = f'Lambda execution completed. Files in bucket: {files}'\n"
                                        "    print(message)\n"
                                        "    sns.publish(TopicArn=topic_arn, Message=message)\n"
                                        "    return {'statusCode': 200, 'body': 'Done'}"
                                    ),
                                    environment={
                                        "BUCKET_NAME": bucket.bucket_name,
                                        "TOPIC_ARN": topic.topic_arn,
                                    })
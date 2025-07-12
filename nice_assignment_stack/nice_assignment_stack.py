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

class NiceAssignmentStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # S3 Bucket
        bucket = s3.Bucket(self,
                           "NiceAssignmentBucket",
                           versioned=True,
                           removal_policy=RemovalPolicy.DESTROY,
                           auto_delete_objects=True)

        # SNS Topic
        topic = sns.Topic(self, "NiceAssignmentTopic")
        topic.add_subscription(subs.EmailSubscription("ariel67788@icloud.com")) 

        # IAM Role
        lambda_role = iam.Role(self, "NiceAssignmentLambdaRole",
                               assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"))
        lambda_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole"))
        lambda_role.add_to_policy(iam.PolicyStatement(
            actions=["s3:ListBucket", "sns:Publish"],
               resources=[bucket.bucket_arn,topic.topic_arn]
        ))

        # Lambda Function
        function = _lambda.Function(self, "NiceAssignmentFunction",
                                    runtime=_lambda.Runtime.PYTHON_3_11,
                                    handler="handler.handler",
                                    role=lambda_role,
                                    code=_lambda.Code.from_asset("lambda_code"),
                                    environment={
                                        "BUCKET_NAME": bucket.bucket_name,
                                        "TOPIC_ARN": topic.topic_arn,
                                    })
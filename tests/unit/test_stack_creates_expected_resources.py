import aws_cdk as core
import aws_cdk.assertions as assertions

from nice_assignment_stack.nice_assignment_stack import NiceAssignmentStack

def test_nice_assignment_stack_resources():
    app = core.App()
    stack = NiceAssignmentStack(app, "nice-assignment-stack")
    template = assertions.Template.from_stack(stack)

    # Check that an S3 bucket is created
    template.resource_count_is("AWS::S3::Bucket", 1)

    # Check that an SNS topic is created
    template.resource_count_is("AWS::SNS::Topic", 1)

    # Check that there is at least one Lambda function with the correct handler
    template.has_resource_properties("AWS::Lambda::Function", {
        "Handler": "handler.handler"
    })
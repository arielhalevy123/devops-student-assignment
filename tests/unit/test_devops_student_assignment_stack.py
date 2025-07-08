import aws_cdk as core
import aws_cdk.assertions as assertions

from devops_student_assignment.devops_student_assignment_stack import DevopsStudentAssignmentStack

# example tests. To run these tests, uncomment this file along with the example
# resource in devops_student_assignment/devops_student_assignment_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DevopsStudentAssignmentStack(app, "devops-student-assignment")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

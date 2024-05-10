import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_lambda_slack.cdk_lambda_slack_stack import CdkLambdaSlackStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_lambda_slack/cdk_lambda_slack_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkLambdaSlackStack(app, "cdk-lambda-slack")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

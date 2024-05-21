from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway  as apigw,
)
from constructs import Construct
from dotenv import load_dotenv
import os

class CdkLambdaSlackStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Load all environment variables from .env file into os.environ
        load_dotenv()

        # Defines a lambda function
        lambda_fn = _lambda.Function(
            self, "LambdaSlackHandler",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="lambda_handler.lambda_handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={
                'SLACK_SIGNING_SECRET': os.environ['SLACK_SIGNING_SECRET'],
                'SLACK_BOT_TOKEN': os.environ['SLACK_BOT_TOKEN']
            }
        )

        # Define API Gateway
        api = apigw.LambdaRestApi(
            self, "Endpoint",
            handler=lambda_fn,
            description="API Gateway for Slack bot",
            proxy=False
        )

        # Define /slack/events resource path
        slack_events_resource = api.root.add_resource("slack").add_resource("events")

        # Add POST method to /slack/events
        slack_events_resource.add_method("POST", integration=apigw.LambdaIntegration(lambda_fn)) 
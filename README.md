# Slack Bot with Slack Bolt, AWS Lambda, and AWS CDK

# Overview

This project is a Slack bot built using the Slack Bolt framework for Python, AWS Lambda, and AWS Cloud Development Kit (CDK). The bot listens to all events in the channels it has been invited to and replies back to users with the text of their message.

# Features

- Event Listening: The bot listens to all events in the channels where it is present.
- Automated Replies: The bot responds to user messages with the text of the user's message, providing a simple echo functionality.
- Serverless Architecture: Utilizing AWS Lambda for serverless execution.
- Infrastructure as Code: Managed and deployed using AWS CDK for streamlined and repeatable infrastructure setup.

# Technology Stack

- Slack Bolt for Python: A framework for building Slack apps in Python.
- AWS Lambda: A serverless compute service that runs your code in response to events.
- AWS CDK (Cloud Development Kit): An open-source software development framework for defining cloud infrastructure in code.

# Getting Started

# Prerequisites

1. Python 3.12+
2. AWS Account
3. AWS CDK

# Installation

1. Clone the Repository

```
$ git clone https://github.com/AnastasiaFilatova/aws_cdk_slakc_bolt_python_app.git
$ cd aws_cdk_slakc_bolt_python_app
```

2. Activate virtual environment

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

3. Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

4. At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

5. Deploy app.

```
$ cdk deploy
```

6. Get the Endpoint URL

After running the cdk deploy command, you should see the output with your Lambda's endpoint URL. It will look something like this:

```
Outputs:
CdkLambdaSlackStack.Endpoint = https://your_endpoint_here.amazonaws.com/prod//slack/events
```

Copy this URL address, you will use it later in the Slack app configuration.

## Useful AWS CDK commands

- `cdk ls` list all stacks in the app
- `cdk synth` emits the synthesized CloudFormation template
- `cdk deploy` deploy this stack to your default AWS account/region
- `cdk diff` compare deployed stack with current state
- `cdk docs` open CDK documentation

# Configuration of a Slack App

1. Create a new Slack app by following instructions from the slack guide https://slack.dev/bolt-python/tutorial/getting-started-http

2. Enable the necessary permissions in and event subscriptions.

- Navigate to the **OAuth & Permissions** on the left sidebar and scroll down to the **Bot Token Scopes** section. Click **Add an OAuth Scope**.
- Add write to chat permission: `[chat:write](https://api.slack.com/scopes/chat:write)`. This grants your app the permission to post messages in channels it’s a member of.

- Navigate to **Event Subscriptions** on the left sidebar and toggle to enable. Under **Subscribe to Bot Events**, you can add events for your bot to respond to. There are four events related to messages:

* `[message.channels](https://api.slack.com/events/message.channels)` listens for messages in public channels that your app is added to
* `[message.groups](https://api.slack.com/events/message.groups)` listens for messages in 🔒 private channels that your app is added to
* `[message.im](https://api.slack.com/events/message.im)` listens for messages in your app’s DMs with users
* `[message.mpim](https://api.slack.com/events/message.mpim)` listens for messages in multi-person DMs that your app is added to

If you want your bot to listen to messages from everywhere it is added to, choose all four message events. After you’ve selected the events you want your bot to listen to, click the green **Save Changes** button.

Add your lambda's endpoint in the request url field. Your URL should become verified.

3. Add the bot to your desired Slack channels.

4. Create .env file in the root of the project, add there slack signing secret and slack bot token in the following format:

```
$ SLACK_SIGNING_SECRET = <your signing secret>
$ SLACK_BOT_TOKEN = <your bot token>
```

Enjoy!

import os
import json
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler


# Load all environment variables from .env file into os.environ
load_dotenv()

# Initializes your app with your bot token and signing secret
# process_before_response must be True when running on FaaS
app = App(token=os.environ.get("SLACK_BOT_TOKEN"),
          signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
          process_before_response=True)

# Listens to all incoming messages and says something back
# To learn available event types,
# visit https://api.slack.com/events?query=me&filter=Events
@app.event("message")
def handle_user_message(body, say):
    print('body: {}'.format(json.dumps(body)))
    text = body["event"]["text"]
    say(text)

def lambda_handler(event, context):
    slack_handler = SlackRequestHandler(app=app)
    return slack_handler.handle(event, context)
import config.config as config
import slack_sdk as slack
import base64
SLACK_BOT_TOKEN = config.slack['bot_token']
client = slack.WebClient(token=SLACK_BOT_TOKEN)

def send_slack_message(message, file):
    # check if slack enabled
    if not config.slack['enabled']:
        return

    # add message to blocks
    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": message
            }
        },
        # add button to create jira ticket with /jira command and pass the file as an argument
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Create Jira Ticket"
                    },
                    "value": "/jira "
                }
            ]
        }
    ]


    ## add file if provided
    if file:
        # upload file to slack
        with open(file, "rb") as f:
            response = client.files_upload(
                channels=config.slack['channel'],
                file=f,
                filename=file,
                initial_comment=message,
                icon_emoji=config.slack['icon_emoji'],
                username=config.slack['username'],
                title=file,
                blocks=blocks
            )
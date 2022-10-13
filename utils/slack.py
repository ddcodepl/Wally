import config.config as config
import slack_sdk as slack

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
    ]

    ## add file if provided
    if file:
        blocks.append({
            "type": "image",
            "image_url": file,
            "alt_text": "Screenshot",
            "title": {
                "type": "plain_text",
                "text": "Screenshot",
                "emoji": True
            }
        })

    # send slack message
    response = client.chat_postMessage(
        channel=config.slack['channel'],
        text=message,
        username=config.slack['username'],
        icon_emoji=config.slack['icon_emoji'],
        blocks=blocks
    )

    assert response["ok"]
    assert response["message"]["text"] == message
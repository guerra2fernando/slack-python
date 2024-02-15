import os
from slack_bolt import App
from slack_sdk.errors import SlackApiError

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Listens to team_join events to send a welcome message to new users
@app.event("team_join")
def handle_team_join(event, say):
    try:
        welcome_text = "Welcome to the team! 🎉 We're glad you're here."
        user_id = event['user']
        say(text=welcome_text, channel=user_id)
    except SlackApiError as e:
        print(f"Error sending message: {e}")

# Listens to member_joined_channel events to send a message when a user joins a specific channel
@app.event("member_joined_channel")
def handle_member_joined_channel(event, say):
    try:
        if event['channel'] == 'C0611FJ6Q4T':
            channel_welcome_text = "Welcome to this channel! 🌟"
            say(text=channel_welcome_text, channel=event['channel'])
    except SlackApiError as e:
        print(f"Error sending message: {e}")

# Start your app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.start(port=port)

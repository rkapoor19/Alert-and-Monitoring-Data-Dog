# Alert-and-Monitoring-Data-Dog

To generate Python code for creating alerts and monitoring through Datadog, and sending notifications to Slack and Microsoft Teams, we'll use the Datadog API to create monitors and configure alert notifications. The Python script will:

Create Datadog Monitors (for specific conditions like CPU usage, memory usage, etc.).
Send notifications to Slack and Microsoft Teams when an alert is triggered.
To do this, you'll need the following:

Datadog API and Application Keys.
Slack Webhook URL and Microsoft Teams Webhook URL.
Python libraries: datadog, requests.
Prerequisites
Install the datadog and requests libraries if you haven't already:

bash
Copy
pip install datadog requests
Obtain your Datadog API and Application keys from the Datadog API Settings.

Set up your Slack and Teams incoming webhooks.
Use Notifucation.py for pythincode tp notify Slack and teams


Explanation of the Code:
Datadog Initialization:

The initialize_datadog() function initializes the Datadog API using your DATADOG_API_KEY and DATADOG_APP_KEY stored in environment variables.
Create Datadog Monitor:

The create_datadog_monitor() function creates a monitor in Datadog based on the query provided. For example, this query checks if the average CPU usage in the last 5 minutes is less than 20% (you can modify the query to match your needs).
The monitor will trigger a critical alert if the threshold is met.
Configure Notifications:

The configure_notifications() function sends notifications to both Slack and Teams using webhooks.
The Slack message is a simple JSON with a text field.
The Teams message follows the MessageCard format, which is compatible with Microsoft Teams' webhook integration.
Main Logic:
The main() function initializes Datadog, creates the monitor, and sends notifications to Slack and Teams.


Setting Environment Variables:
To run the script successfully, make sure to set the necessary environment variables for your Datadog API keys and webhook URLs. For example, in your terminal:

bash
Copy
export DATADOG_API_KEY='your_datadog_api_key'
export DATADOG_APP_KEY='your_datadog_app_key'
export SLACK_WEBHOOK_URL='your_slack_webhook_url'
export TEAMS_WEBHOOK_URL='your_teams_webhook_url'
Customization:
Datadog Monitor Query: Change the query in the create_datadog_monitor() function to set the specific metric and threshold for your use case.
Slack and Teams Payload: Modify the slack_payload and teams_payload variables to adjust the notification format and message according to your needs.
Running the Script:
Once you have the environment variables set, you can run the script like so:

bash
Copy
python datadog_alerts.py
This will create a Datadog monitor for CPU usage, and when triggered, it will send a notification to both Slack and Microsoft Teams.

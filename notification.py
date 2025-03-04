import os
import json
import requests
from datadog import initialize, api

# Initialize Datadog API client with your API and Application keys
def initialize_datadog():
    options = {
        'api_key': os.getenv('DATADOG_API_KEY'),
        'app_key': os.getenv('DATADOG_APP_KEY')
    }
    initialize(**options)

# Function to create Datadog monitor (e.g., for CPU usage)
def create_datadog_monitor():
    # Define the alert condition for CPU usage
    monitor_options = {
        "name": "High CPU Usage Alert",
        "type": "metric alert",
        "query": "avg(last_5m):avg:system.cpu.idle{*} by {host} < 20",  # Alert for CPU usage < 20%
        "message": "CPU usage is too high on host {{host.name}}. Please check the system.",
        "tags": ["env:production", "team:infra"],
        "priority": 2,
        "notify_no_data": True,
        "no_data_timeframe": 10,
        "renotify_interval": 60,
        "thresholds": {
            "critical": 20
        },
        "notify_audit": False,
        "escalation_message": "Please check the Datadog dashboard for more details.",
    }

    # Create the monitor in Datadog
    response = api.Monitor.create(**monitor_options)
    print(f"Monitor created with ID: {response['id']}")
    return response['id']

# Function to set up Slack and Teams notifications for Datadog monitor
def configure_notifications(monitor_id):
    # Webhook URLs for Slack and Teams (replace with your actual URLs)
    slack_webhook_url = os.getenv('SLACK_WEBHOOK_URL')
    teams_webhook_url = os.getenv('TEAMS_WEBHOOK_URL')

    # Prepare the notification message (You can customize this)
    notification_message = f"Datadog Monitor Triggered: High CPU usage on monitor ID {monitor_id}. Please check the system."

    # Send notification to Slack
    slack_payload = {
        "text": notification_message
    }
    requests.post(slack_webhook_url, json=slack_payload)

    # Send notification to Teams
    teams_payload = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "text": notification_message
    }
    requests.post(teams_webhook_url, json=teams_payload)

# Main function to initialize Datadog and create monitor with notifications
def main():
    # Initialize Datadog
    initialize_datadog()

    # Create the Datadog monitor
    monitor_id = create_datadog_monitor()

    # Configure the Slack and Teams notifications
    configure_notifications(monitor_id)

if __name__ == '__main__':
    main()

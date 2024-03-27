"""
This file is used to clean up the dashboards exported from Grafana.

1. Rename the file to remove the suffix and timestamp
2. Edit the `uid` of the dashboard back to the original
3. Add tags to the dashboard

(c) 2024 Seventh State
"""
import glob
import re
import os
import json

dashboard_config = {
    "Clusters": {
        "tags": ["rabbitmq-prometheus", "7s-rabbitmq-support"],
        "uid": "7s-rabbitmq-clusters"
    },
    "Connections Overview": {
        "tags": ["rabbitmq-prometheus", "7s-rabbitmq-support"],
        "uid": "7s-rabbitmq-connections-overview"
    },
    "Channels Overview": {
        "tags": ["rabbitmq-prometheus", "7s-rabbitmq-support"],
        "uid": "7s-rabbitmq-channels-overview"
    },
    "Queues Overview": {
        "tags": ["rabbitmq-prometheus", "7s-rabbitmq-support"],
        "uid": "7s-rabbitmq-queues-overview"
    },
    "Queue Details": {
        "tags": ["rabbitmq-prometheus", "7s-rabbitmq-support"],
        "uid": "7s-rabbitmq-queue-details"
    },
    "Investigation Metrics": {
        "tags": ["rabbitmq-prometheus", "7s-rabbitmq-support"],
        "uid": "7s-rabbitmq-investigation-metrics"
    },
}

print('\n'.join(list(dashboard_config)))

# Rename WIP exported dashboards to their original name
wip_dashboards = glob.glob('**/*.json', recursive=True)

for wip_dashboard in wip_dashboards:
    print(f"Processing {wip_dashboard}")
    # Replace the pattern 'WIP-timestamp' with an empty string using regular expression
    dashboard = re.sub(r'( Copy)?-[0-9]*\.json', '.json', wip_dashboard)
    # Rename the file
    os.rename(wip_dashboard, dashboard)

for dashboard, config in dashboard_config.items():
    print(f"Setting configuration on {dashboard}")


    filename = f"RabbitMQ {dashboard} - Seventh State RabbitMQ Support.json"

    if not os.path.isfile(filename):
        print(f"File not found: {filename}")
        continue

    f = open(filename)
    dash = json.load(open(filename))
    f.close()

    dash['uid'] = config['uid']
    dash['tags'] = config['tags']

    title = f"RabbitMQ {dashboard} - Seventh State RabbitMQ Support"
    dash["title"] = title

    json.dump(dash, open(f"{title}.json", 'w'), indent=2, sort_keys=True)

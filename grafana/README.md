
# Dashboards

The source code of Grafana Dashboards created by Seventh State RabbitMQ Support.

For more information on how to use the dashboards, please visit https://seventhstate.io/rabbitmq-monitoring-dashboards.

These dashboards are available for download from the Grafana Website: \
https://grafana.com/orgs/seventhstate

## Metrics Used in Dashboards

The detailed metrics used in these dashboards are grouped under the followings:

- channel_metrics
- connection_coarse_metrics
- queue_coarse_metrics
- queue_consumer_count
- queue_delivery_metrics
- queue_exchange_metrics

## Editing the Grafana Dashboards

1. Provisioned dashboards can not be edited - they have to be copied
    1. Choose the dashboard you want to edit
    2. Click the  ⚙ (gear) icon on the top right of the dashboard
    3. Click `Save as` in the top right
    4. Save the dashboard with "Copy" in the name
2. After editing is done, external export the dashboard
3. Run the script `python3 fix-dashboards.py`, this will
    1. Rename the file to remove the `Copy` suffix and timestamp
    2. Edit the `uid` of the dashboard back to the original
    3. Add tags to the dashboard


# LICENSE

These resources are subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Copyright
(c) 2024 Seventh State. All Rights Reserved.

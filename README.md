# Sleep-monitor

## Description
Our smart stress detection system provides real-time monitoring of various health metrics collected in and through sleep to indicate stress levels to the users. The system collects data from multiple sensors and visualizes it on a user-friendly Grafana dashboard. Specifically, the system tracks and visualizes snoring range, limb movement rate, respiration rate, hours of sleep, body temperature, eye movement, heart rate, blood oxygen level, and stress levels. 

Users need to log in to the Grafana dashboard to view their health metrics related to their sleeping patterns. The dashboard refreshes autonomously to display real-time data, so users don't need to do anything else. Additionally, the displayed data includes time series, allowing users to check their metrics over various periods.

This system is dedicated to the movement towards a healthier lifestyle. Nowadays, fitness bands help people maintain a more active lifestyle. However, quality sleep is just as important as regular exercise for maintaining a healthy body. Thus, through this system, people can better understand their sleeping patterns and adjust their lifestyles to achieve healthier bodies. This system can also be highly appreciated by healthcare providers, as having a good understanding of patients' sleeping patterns can assist in diagnosing various health complexities.

## Setup
1. Run the project
    - Go to project in terminal
    - Execute `Docker-compose up -d`
2. Log in to InfluxDB
    - Go to `localhost:8086`
    - Log in
        - Username: admin
        - Password: admin123
3. Log in to Grafana
    - Go to `localhost:3000`
    - Log in
        - Username: admin
        - Password: admin
    - Press `Skip`
4. Create bucket
    - Hover over the upward arrow in the leftside panel and go to `Buckets`
	- Press `+ CREATE BUCKET`
        - Name the bucket `SleepMonitor`
5. Set up Telegraf API token
    - Hover over the upward arrow in the leftside panel and go to `API Tokens`
    - Press `+ GENERATE API TOKEN` and select `Cusom API Token`
        - Allow `write` for `Buckets` > `SleepMonitor`
        - Allow `read` from `Telegrafs` > `All Telegrafs`
    - Optional: Describe the token as `Telegraf`
    - Press `Copy to clipboard`
    - Go to the project's .env file
    - Change the `INFLUX_TOKEN` to the generated Telegraf API token (in the clipboard)
6. Set up Grafan API token
    - Go back to `localhost:8086`
    - Hover over the upward arrow in the leftside panel and go to `API Tokens`
    - Press `+ GENERATE API TOKEN` and select `Cusom API Token`
        - Allow `read` from `Buckets` > `SleepMonitor`
    - Optional: Describe the token as `Grafana`
    - Press `Copy to clipboard`
    - Go to the project's .env file
    - Change the `GRAFANA_INFLUX_TOKEN` to the generated API token (in the clipboard)
    - Go to `localhost:3000` (repeat step 3 when logged out)
    - Go to `configuration` > `InfluxDB`
    - Under `InfluxDB Details`, change `Token` to the generated Grafana API Token (in the clipboard)
    - Press `Save & test`
7. Run the project
    - Save the .env file
    - Go to project in terminal
    - Execute `Docker-compose down`
    - Execute `Docket compose up`
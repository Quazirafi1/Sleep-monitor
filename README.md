# Sleep-monitor

## Description
Our smart stress detection system provides real-time monitoring of various health metrics collected in and through sleep to indicate stress levels to the users. The system collects data from multiple sensors and visualizes it on a user-friendly Grafana dashboard. Specifically, the system tracks and visualizes snoring range, limb movement rate, respiration rate, hours of sleep, body temperature, eye movement, heart rate, blood oxygen level, and stress levels. 

Users need to log in to the Grafana dashboard to view their health metrics related to their sleeping patterns. The dashboard refreshes autonomously to display real-time data, so users don't need to do anything else. Additionally, the displayed data includes time series, allowing users to check their metrics over various periods.

This system is dedicated to the movement towards a healthier lifestyle. Nowadays, fitness bands help people maintain a more active lifestyle. However, quality sleep is just as important as regular exercise for maintaining a healthy body. Thus, through this system, people can better understand their sleeping patterns and adjust their lifestyles to achieve healthier bodies. This system can also be highly appreciated by healthcare providers, as having a good understanding of patients' sleeping patterns can assist in diagnosing various health complexities.

## Setup
Go to project in terminal
	Docker-compose up
Go to localhost:8086
Enter admin -> admin123
Go to Buckets
	      Create bucket ’SleepMonitor’
Go to API tokens
Generate custom API token
        - ‘Telegraf’
            - Write to sleepMonitor
            - Read from all telegrafs
Go to .env
	Change INFLUX_TOKEN to the generated API token
Go to localhost:8086
Go to API tokens
Generate custom API token
    - ‘Grafana’
        - Read from sleepMonitor
Go to .env
	Change GRAFANA_INFLUX_TOKEN to the generated API token
Save .env
Go to localhost:3000
	Go to configuration
		Go to InfluxDB Details
			Change Token to generated API token
			Press ‘Save & test’
Go to running project terminal
	Enter ctrl+C
	Run docker-compose up
#!/bin/bash

# Protects script from continuing with an error
set -eu -o pipefail

# Ensures environment variables are set
export INFLUXDB_USERNAME=$INFLUXDB_USERNAME
export INFLUXDB_PASSWORD=$INFLUXDB_PASSWORD
export INFLUXDB_ORG=$INFLUXDB_ORG
export INFLUXDB_BUCKET=$INFLUXDB_BUCKET
export INFLUXDB_RETENTION=$INFLUXDB_RETENTION
export INFLUXDB_ADMIN_TOKEN=$INFLUXDB_ADMIN_TOKEN
export INFLUXDB_PORT=$INFLUXDB_PORT
export INFLUXDB_IP=$INFLUXDB_IP

# Conducts initial InfluxDB using the CLI
influx setup --skip-verify --bucket ${DOCKER_INFLUXDB_INIT_BUCKET} --retention ${DOCKER_INFLUXDB_INIT_RETENTION} --token ${DOCKER_INFLUXDB_INIT_ADMIN_TOKEN} --org ${DOCKER_INFLUXDB_INIT_ORG} --username ${DOCKER_INFLUXDB_INIT_USERNAME} --password ${DOCKER_INFLUXDB_INIT_PASSWORD} --host http://${INFLUXDB_IP}:${INFLUXDB_PORT} --force

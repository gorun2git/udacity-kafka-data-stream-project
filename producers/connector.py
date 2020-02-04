"""Configures a Kafka Connector for Postgres Station data"""
import json
import logging

import requests

import config

logger = logging.getLogger(__name__)


def configure_connector():
    """Starts and configures the Kafka Connect connector"""
    logging.debug("creating or updating kafka connect connector...")

    resp = requests.get(f"{config.KAFKA_CONNECT_URL}/{config.CONNECTOR_NAME}")
    if resp.status_code == 200:
        logging.debug("connector already created skipping recreation")
        return
    resp = requests.post(
       config.KAFKA_CONNECT_URL,
       headers={"Content-Type": "application/json"},
       data=json.dumps({
           "name": config.CONNECTOR_NAME,
           "config": {
               "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
               "key.converter": "org.apache.kafka.connect.json.JsonConverter",
               "key.converter.schemas.enable": "false",
               "value.converter": "org.apache.kafka.connect.json.JsonConverter",
               "value.converter.schemas.enable": "false",
               "batch.max.rows": "500",
               "connection.url": config.POSTGRES_CONNECTION_STRING,
               "connection.user": config.POSTGRES_USER,
               "connection.password": config.POSTGRES_PASS,
               "table.whitelist": "stations",
               "mode": "incrementing",
               "incrementing.column.name": "stop_id",
               "topic.prefix": config.CONNECTOR_TOPIC_PREFIX,
               "poll.interval.ms": "60000",
           }
       }),
    )

    ## Ensure a healthy response was given
    resp.raise_for_status()
    logging.debug("connector created successfully")


if __name__ == "__main__":
    configure_connector()

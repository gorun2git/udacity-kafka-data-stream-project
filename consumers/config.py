
# Broker
BROKER_URL = "PLAINTEXT://localhost:9092"
SCHEMA_REGISTRY_URL = "http://localhost:8081"

# KSQL
KSQL_URL = "http://localhost:8088"

# Faust
FAUST_BROKER_URL = "kafka://localhost:9092"

# Kafka connect
CONNECTOR_NAME = "stations"
CONNECTOR_TOPIC_PREFIX = "com.udacity.cta.gs.topic.connect."

# Tornado webserver
WEB_SERVER_PORT = 8889

# Topics
TOPIC_STATIONS = "com.udacity.cta.gs.topic.stations"
TOPIC_TURNSTILE = "com.udacity.cta.gs.topic.turnstile"
TOPIC_WEATHER = "com.udacity.cta.gs.topic.weathers"
TOPIC_FAUST_TABLE = "com.udacity.cta.gs.topic.connect.stations.table"
TOPIC_TURNSTILE_SUMMARY = "TURNSTILE_SUMMARY"
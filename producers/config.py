
# Broker
BROKER_URL = "PLAINTEXT://localhost:9092"
SCHEMA_REGISTRY_URL = "http://localhost:8081"

# Kafka connect
KAFKA_CONNECT_URL = "http://localhost:8083/connectors"
CONNECTOR_NAME = "stations"
CONNECTOR_TOPIC_PREFIX = "com.udacity.cta.gs.topic.connect."

# Postgres
POSTGRES_CONNECTION_STRING = "jdbc:postgresql://localhost:5432/cta"
POSTGRES_USER = "cta_admin"
POSTGRES_PASS = "chicago"

# Rest proxy
REST_PROXY_URL = "http://localhost:8082"

# Topics
TOPIC_STATIONS = "com.udacity.cta.gs.topic.stations"
TOPIC_TURNSTILE = "com.udacity.cta.gs.topic.turnstile"
TOPIC_WEATHER = "com.udacity.cta.gs.topic.weathers"
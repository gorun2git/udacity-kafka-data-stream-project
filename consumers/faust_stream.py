"""Defines trends calculations for stations"""
import logging

import faust


logger = logging.getLogger(__name__)


# Faust will ingest records from Kafka in this format
class Station(faust.Record):
    stop_id: int
    direction_id: str
    stop_name: str
    station_name: str
    station_descriptive_name: str
    station_id: int
    order: int
    red: bool
    blue: bool
    green: bool


# Faust will produce records to Kafka in this format
class TransformedStation(faust.Record):
    station_id: int
    station_name: str
    order: int
    line: str


app = faust.App("stations-stream", broker="kafka://localhost:9092", store="memory://")
topic = app.topic("com.udacity.cta.gs.topic.connect.stations", value_type=Station)
out_topic = app.topic("com.udacity.cta.gs.topic.connect.stations.table", partitions=1)
table = app.Table(
   "station_transformated",
   default=int,
   partitions=1,
   changelog_topic=out_topic,
)


@app.agent(topic)
async def transformstation(stations):
    async for station in stations:
        station_id = station.station_id
        station_name = station.station_name
        order = station.order
        if station.red:
            line = "red"
        elif station.blue:
            line = "blue"
        else:
            line = "green"
        transformed = TransformedStation(station_id,
                                         station_name,
                                         order, line)
        await out_topic.send(key=transformed.station_name,
                             value=transformed)


if __name__ == "__main__":
    app.main()

"""Contains functionality related to Lines"""
import json
import logging

from models import Line


logger = logging.getLogger(__name__)


class Lines:
    """Contains all train lines"""

    def __init__(self):
        """Creates the Lines object"""
        self.red_line = Line("red")
        self.green_line = Line("green")
        self.blue_line = Line("blue")

    def process_message(self, message):
        """Processes a station message"""
        # if "org.chicago.cta.station" in message.topic():
        if "com.udacity.cta.gs.topic.stations" in message.topic():
            value_message = message.value()
            #if message.topic() == "org.chicago.cta.stations.table.v1":
            if message.topic() == "com.udacity.cta.gs.topic.connect.stations.table":
                value_message = json.loads(value_message)
            if value_message["line"] == "green":
                self.green_line.process_message(message)
            elif value_message["line"] == "red":
                self.red_line.process_message(message)
            elif value_message["line"] == "blue":
                self.blue_line.process_message(message)
            else:
                logger.debug("discarding unknown line msg %s", value_message["line"])
        elif "TURNSTILE_SUMMARY" == message.topic():
            self.green_line.process_message(message)
            self.red_line.process_message(message)
            self.blue_line.process_message(message)
        else:
            logger.info("ignoring non-lines message %s", message.topic())

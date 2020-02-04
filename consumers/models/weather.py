"""Contains functionality related to Weather"""
import logging


logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def _handle_weather_value(self,value):
        """Handle weather data"""
        self.temperature = value["temperature"]
        self.status = value["status"]

    def process_message(self, message):
        """Handles incoming weather data"""
        try:
            value = message.value()
            self._handle_weather_value(message.value())
        except Exception as e:
            logger.fatal("bad weather? %s, %s", value, e)

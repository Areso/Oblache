from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import WriteOptions
import logging


class Config:
    pacing_sec = 0.1
    api_host = 'https://dbend.areso.pro'
    influx_client = InfluxDBClient(url="https://dbend.areso.pro")
    influxdb = influx_client.write_api(write_options=WriteOptions(batch_size=10,
                                                                  flush_interval=10_000,
                                                                  jitter_interval=2_000,
                                                                  retry_interval=5_000, ))


class LogConfig:
    logger = logging.getLogger('demo_logger')
    logger.setLevel('DEBUG')
    file = logging.FileHandler(filename='test_logs.log')
    file.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
    logger.addHandler(file)
    logger.propagate = False


logger = LogConfig().logger
cfg = Config()

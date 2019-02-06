#!usr/bin/env python

"""
Config manager for etl

"""

import logging
import os

logging.getLogger(__name__)

class Config(object):
    pass

class DevelopmentConfig(Config):
    logging.info("Loaded DEV configs")
    DEBUG = True
    AWS_REGION = "us-east-1"

    download_folder = os.getcwd() + os.sep + "data"
    file_url = "xxxxxx"

    LOG_LEVEL = logging.INFO
    LOGS_ROOT = "/logs"

    batch_size = 200

    pg_db = {"pg_data_lake": {"dbname": "xxxx",
                              "user": "xxxx",
                              "host": "xxxx",
                              "password": "xxxx",
                              "port": "xxxx"

                                 }}
    lambda_base_url = "xxxx"


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    pass

conf = {
    'DEV': DevelopmentConfig,
    'PROD': ProductionConfig,
    'TEST': TestingConfig
}


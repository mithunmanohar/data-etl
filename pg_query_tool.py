"""
Invokes the aws lambda function through Amazon api gateway and returns
the results
"""

import os
import requests
from configs.config import conf

class DataBaseClient(object):
    def __init__(self, configs):
        self.configs = configs

    def query_database(self, query):
        lambda_base_url = self.configs.lambda_base_url
        lambda_url  = lambda_base_url + "query=" + query

        request = requests.get(lambda_url)

        result = request.text

        return result

if __name__ == '__main__':
    ENV = os.getenv('ENVIRONMENT', 'DEV')                               # fetch platform from env
    configs = conf[ENV]
    db_client = DataBaseClient(configs)
    print(db_client.query_database("select * from twitter LIMIT 10"))
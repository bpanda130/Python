import requests
import csv
import logging as logger
import json

from EXERCISES.APIGetCSVWrite.constants import LOGS_DIR, OUTPUTS_DIR, CONF_DIR
logger.basicConfig(filename=LOGS_DIR + 'API.log', level=logger.INFO, datefmt='%Y-%m-%d %H:%M:%S')

# def log_args(func):
#
#     """This decorator dumps out the arguments passed to a function before calling it"""
#
#     def echo_func_args():
#         inspect.getfullargspec(func)
#         return echo_func_args


class APIHelper():

    def __init__(self, url):
        self.url = url
        with open(CONF_DIR + 'api.conf', 'r') as conf:
            self.columns = json.load(conf)["result_keys"]


    def star_wars_characters(self):
        api_response = requests.get(self.url)
        if api_response.status_code == 200:
            output = []
            for column_val in api_response.json()['results']:
                output.append([x for x in map(lambda x: column_val[x], self.columns)])
            return output
        else:
            return api_response.reason

    # @log_args
    def append_to_file(self, file_name):

        with open(OUTPUTS_DIR + file_name, "w") as file_w:
            csv_file = csv.writer(file_w, delimiter=',')
            # write the header for the csv file - only once
            csv_file.writerow([x.title() for x in self.columns])
            for row in self.star_wars_characters():
                csv_file.writerow(row)
        logger.info("Finished writing to file : {}".format(file_name))
        file_w.close()

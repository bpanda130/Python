import requests
import csv
import logging as logger
import datetime
import sys

from EXERCISES.APIGetCSVWrite.constants import *
logger.basicConfig(filename=LOGS_DIR + 'API.log', level=logger.INFO, datefmt='%Y-%m-%d %H:%M:%S')

# class log(object):
#     def __init__(self, func):
#         self.func = func
#
#     def log_args(self, *args, **kwargs):
#         log_path = os.path.join(LOGS_DIR, 'API.log')
#         print("\n Log file Location : " + log_path)
#         argnames = args[0]
#         print(argnames)
#         start = datetime.datetime.now()
#         Tem = self.func(*args)
#         FunName = self.func.__name__
#         end = datetime.datetime.now()
#
#         message = """
#                     Function        : {}
#                     Execustion Time : {}
#                     Memory          : {} Bytes
#                     Date            : {}
#                     """.format(FunName,
#                                #argnames,
#                                end-start,
#                                sys.getsizeof(self.func),
#                                start)
#         logger.info(message)
#         print(message)
#         return Tem


class APIHelper():

    def __init__(self, url):
        self.url = url
        self.columns = ["name", "height", "gender"]

    def star_wars_characters(self):
        api_response = requests.get(self.url)
        if api_response.status_code == 200:
            output = []
            for column_val in api_response.json()['results']:
                output.append([x for x in map(lambda x: column_val[x], self.columns)])
            return output
        else:
            return api_response.reason

    #@log
    def append_to_file(self, file_name):
        file_path = os.path.join(OUTPUTS_DIR, file_name)
        with open(file_path, "w") as file_w:
            csv_file = csv.writer(file_w, delimiter=',')
            csv_file.writerow([x.title() for x in self.columns])
            for row in self.star_wars_characters():
                csv_file.writerow(row)
        logger.info("Finished writing to file : {}".format(file_path))
        file_w.close()

'''
Created on Dec 21, 2022
@author: GEETA PANCHAL
'''
import os
import sys
import datetime
import logging
from config import configuration


class Logging:
    logfile_Name = configuration.logfile_name
    now = datetime.datetime.now()
    datenow = now.strftime("%d-%m-%Y")

    # set logfile path
    reportpath = sys.path[0] + os.sep + "logs" + os.sep + logfile_Name + '_' + datenow + '.log'

    # set logging format
    FORMAT = '[ %(asctime)s ] - %(levelname)s : %(name)s :  %(message)s'
    logging.basicConfig(level=logging.INFO, filename=reportpath, filemode='w', format=FORMAT)

    def logError(self, message):
        logging.error(message)

    def logWarning(self, message):
        logging.warning(message)

    def logInfo(self, message):
        print(message)
        logging.info(message)

    def logDebug(self, message):
        logging.debug(message)

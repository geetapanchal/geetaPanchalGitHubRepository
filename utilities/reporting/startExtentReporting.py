import os
import sys
import jpype as jp
import datetime
from config import configuration


class StartReporting:
    try:
        now = datetime.datetime.now()
        datenow = now.strftime("%d-%m-%Y")
        ReportName = configuration.ExtentReport_name
        # set classpath
        bson = sys.path[0] + os.sep + "lib" + os.sep + 'bson-3.3.0.jar'
        extent = sys.path[0] + os.sep + "lib" + os.sep + 'extentreports-2.41.2.jar'
        freemaker = sys.path[0] + os.sep + "lib" + os.sep + 'freemarker-2.3.23.jar'
        jsoup = sys.path[0] + os.sep + "lib" + os.sep + 'jsoup-1.9.2.jar'
        mongodrive = sys.path[0] + os.sep + "lib" + os.sep + 'mongodb-driver-3.3.0.jar'
        mongocore = sys.path[0] + os.sep + "lib" + os.sep + 'mongodb-driver-core-3.3.0.jar'
        sqlite = sys.path[0] + os.sep + "lib" + os.sep + 'sqlite-jdbc-3.8.11.1.jar'
        classpath = os.pathsep.join((bson, extent, freemaker, jsoup, mongodrive, mongocore, sqlite))

        # start JVM
        jp.startJVM(jp.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % classpath)

        # store extent function
        ExtentReports = jp.JClass('com.relevantcodes.extentreports.ExtentReports')
        ExtentTest = jp.JClass('com.relevantcodes.extentreports.ExtentTest')
        LogStatus = jp.JClass('com.relevantcodes.extentreports.LogStatus')

    except Exception as e:
        print(e)

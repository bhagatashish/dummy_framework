import inspect
import logging

class baseClass:

    def test_logs(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername) # here name means class name
        fileFormat = logging.Formatter("%(asctime)s : %(name)s : %(levelname)s : %(message)s") # used to format the file
        filename = logging.FileHandler('logfile.log') # create or update file name
        filename.setFormatter(fileFormat) # make connection between file name and format file
        logger.addHandler(filename) # linking filename , to make connection between logs and file name path
        logger.setLevel("DEBUG")
        return logger

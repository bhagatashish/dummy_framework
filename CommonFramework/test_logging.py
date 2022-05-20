# in getLogger we should always give arugument __name__. This will help in fecthing name of the test case.
# file formatter arguments needs to me memorized
# logs will always be get printed in sequence order and the default sequence is 'debug', 'info', 'warning','error'
#'critical'
# in order to print logs according to yiour need , you need to pass 'logger.setLevel('DEBUG')'. This way it will
# start logging from debug statement.

import logging


def test_logs():
    logger = logging.getLogger(__name__) # here name means class name
    fileFormat = logging.Formatter("%(asctime)s : %(name)s : %(levelname)s : %(message)s") # used to format the file
    filename = logging.FileHandler('logfile.log') # create or update file name
    filename.setFormatter(fileFormat) # make connection between file name and format file
    logger.addHandler(filename) # linking filename , to make connection between logs and file name path
    logger.setLevel('DEBUG')
    logger.debug("debug logs")
    logger.critical('critical')
    logger.info('info logs')

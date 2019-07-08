

import logging
import logging.handlers

class LogDao():
    @staticmethod
    def save_log_for_error(logger_content):
        logger = logging.getLogger('files')
        if(type(logger_content).__name__ == 'dict'):
            for key in logger_content:
                logger.error(key+":"+logger_content[key])
        if(type(logger_content).__name__ == 'list'):
            for key in logger_content:
                logger.error(key)

    @staticmethod
    def save_log_for_console(logger_content):
        logger = logging.getLogger("scripts")
        logger.debug("dasdasdas")



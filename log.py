"""
Logging functions for log the application info and errors.
Whenever you do:
    pyinstaller --windowed your_app.py #--no-consele
Your app not save/display errors, crashes without any info.
This is for that, log the errors to logs folder.
So user send logs to YOU, and you can fix the issues.
Usage:
# don't forget file_path=__file__ to know which file logged the info
# or module just itself logging
    from log import *
    file = __file__
    log("This is an info message.", file_path=file)
    log("This is a warning message.", detail="WARNING", file_path=file)
    log("This is an error message.", detail="ERROR", file_path=file)
    try:
        hello
    except Exception as e:
        log(str(e), detail="error", file_path=file)

    # full log info from exception object:

    try:
        1 / 0
    except Exception as e:
        loged = get_error_log(e)
        log(loged, detail="ERROR", file_path=file)

    # or use SimpleLog class for no always file_path parameter:
    logger = SimpleLog(file_path=__file__)
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    try:
        hello
    except Exception as e:
        logger.detailed_error(str(e))
"""

import os, datetime, traceback

def log(info, detail="INFO", file_path = __file__):
    """
    Log the info with date and type on logs folder.
    Usage:
        log("This is an info message.")
        log("This is a warning message.", detail="WARNING")
        log("This is an error message.", detail="ERROR")
        try:
            hello
        except Exception as e:
            log(str(e), detail="error")
        
    Useful when make GUI applications, whenever user see error log and report it to you.
    Use as print function! 

    """
    os.makedirs("logs", exist_ok=True)
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    detail = f"[{detail.upper()}]"
    loger = f"\n\nFile {file_path}: {date} {detail}: {info}"
    with open(f"logs/{datetime.datetime.now().strftime('%Y-%m-%d')}.log", "a") as log:
        log.write(loger)

def get_error_log(error, addings="'''\n", start="\n"):
    """
    Gets full log info from an exception object.
    Usage:
        try:
            1 / 0
        except Exception as e:
            loged = get_error_log(e)
            print(loged)
    Whenever your app needs full log info, use this function to get it.
    """
    loger = traceback.format_exception(error)
    return start + addings + "".join(loger) + addings.strip()

class SimpleLog:
    """
    Simple logging class to log info, warnings and errors.
    No need to use file_path parameter always. 
    Usage:
        logger = SimpleLog(file_path=__file__)
        logger.info("This is an info message.")
        logger.warning("This is a warning message.")
        logger.error("This is an error message.")
        try:
            hello
        except Exception as e:
            logger.detailed_error(str(e))
    As like print function, but logs save!
    """
    def __init__(self, file_path=__file__):
        self.file_path = file_path

    def info(self, message):
        log(message, detail="INFO", file_path=self.file_path)

    def warning(self, message):
        log(message, detail="WARNING", file_path=self.file_path)

    def error(self, message):
        log(message, detail="ERROR", file_path=self.file_path)

    def custom(self, message, detail):
        log(message, detail=detail, file_path=self.file_path)
    
    def detailed_error(self, exception):
        log(get_error_log(exception), detail="ERROR", file_path=self.file_path)
    
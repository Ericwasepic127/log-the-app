# Logging functions for log the application info and errors.
Whenever you do:
    pyinstaller --windowed your_app.py
Your app not save/display errors, crashes without any info.
This is for that, log the errors to logs folder.
So user send logs to YOU, and you can fix the issues.
## Usage:
### Don't forget file_path=__file__ to know which file logged the info
### or module just log itself

```python
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
```
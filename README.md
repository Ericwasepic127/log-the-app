# Logging functions for log the application info and errors.
Whenever you do:

```bash
# pyinstaller, making executable without console

pyinstaller --windowed --onefile your_app.py
```

Your app not save/display errors, crashes without any info.

This is for that, log the errors to logs folder.

So user send logs to YOU, and you can fix the issues.
## Usage:
**Don't forget file_path=__file__ to know which file logged the info or module just log itself**

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
## Licence: 
**MIT License**

Copyright (c) 2025 Erkhemee

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.**
## Additional info (may you have to know it)
**FAQ:**
- *Where is log saved?*
  The log is in `folder logs`, on same location of file that created. Logs sorted by date. 

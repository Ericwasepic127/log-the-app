import os, datetime

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
    loger = f"File {file_path}: {date} {detail}: {info}"
    with open("logs/log_file", "a") as log:
        log.write(loger + "\n")

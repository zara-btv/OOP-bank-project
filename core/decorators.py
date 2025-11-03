
from datetime import datetime
import json

def logdecorator(func):
    def wrapper(*args, **kwargs):
        time=datetime.now()
        if args and hasattr(args[0],"owner"):
            owner=args[0].owner
        else:
            owner=getattr(args[0],"_name","System")
        try:
            result = func(*args, **kwargs)
            log_status="SUCCESS"
        except Exception as e:
            result=str(e)
            log_status=f"Exception occured: {type(e).__name__}"
            backup=getattr(args[0],"_backup_balance",None)
            log_entry={
                "time":str(time),
                "owner":owner,
                "function_name":func.__name__,
                "args": [str(a) if not isinstance(a, (int, float, str)) else a for a in args],
                "status": log_status,
                "exception": str(e),
                "rollback": backup
            }
            try:
                with open("log.json","r",encoding="utf-8") as f:
                    logs=json.load(f)
                    if isinstance(logs,dict):
                        logs=[logs]
            except (FileNotFoundError, json.JSONDecodeError):
                logs=[]
            logs.append(log_entry)
            with open("log.json","w",encoding="utf-8") as f:
                json.dump(logs,f,ensure_ascii=False,indent=4)
            raise
        else:
            log_entry={
                "time":str(time),
                "owner":owner,
                "function_name":func.__name__,
                "args": [str(a) if not isinstance(a, (int, float, str)) else a for a in args],
                "result":result,
                "status": log_status,
            }
            try:
                with open("log.json", "r", encoding="utf-8") as f:
                    logs = json.load(f)
                    if isinstance(logs, dict):
                        logs = [logs]
            except (FileNotFoundError, json.JSONDecodeError):
                logs = []

            logs.append(log_entry)
            with open("log.json", "w", encoding="utf-8") as f:
                json.dump(logs, f, ensure_ascii=False, indent=4)
            return result
    return wrapper

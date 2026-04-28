import json
from datetime import datetime

LOG_FILE = "logs/alerts.json"

def log_alert(event_type, severity, message):
    try:
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    new_log = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": event_type,
        "severity": severity,
        "message": message
    }

    data.append(new_log)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=4)

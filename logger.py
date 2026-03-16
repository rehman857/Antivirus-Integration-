import json
from datetime import datetime

LOG_FILE = "logs/alerts.json"

def log_alert(event_type, severity, details):
    alert = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "event_type": event_type,
        "severity": severity,
        "details": details
    }

    try:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(alert) + "\n")
    except Exception as e:
        print("Logging error:", e)


import psutil
from modules.logger import log_alert
import time

# List of suspicious process names
SUSPICIOUS_PROCESSES = [
    "nmap",
    "netcat",
    "hydra",
    "john",
    "msfconsole"
]

def monitor_processes():
    print("[INFO] Process monitoring started...")

    seen_pids = set()

    while True:
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                pid = proc.info['pid']
                name = proc.info['name']

                if pid not in seen_pids:
                    seen_pids.add(pid)

                    print(f"[INFO] Process started: {name}")

                    if name and name.lower() in SUSPICIOUS_PROCESSES:
                        print(f"[ALERT] Suspicious process detected: {name}")
                        log_alert("process_monitor", "HIGH", f"Suspicious process: {name}")

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        time.sleep(2)

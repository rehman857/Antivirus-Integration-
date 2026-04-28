import psutil
import time
from modules.logger import log_alert

def monitor_processes():
    print("[INFO] Process monitoring started...")

    seen_pids = set()

    while True:
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                pid = proc.info['pid']
                name = proc.info['name'] or ""

                try:
                    cmd = " ".join(proc.cmdline()).lower()
                except:
                    cmd = ""

                name_lower = name.lower()

                if "nmap" in name_lower or "nmap" in cmd:

                    if pid in seen_pids:
                        continue

                    seen_pids.add(pid)

                    print(f"[ALERT] Detected: {name} (PID: {pid})")

                    try:
                        proc.terminate()
                        time.sleep(0.2)
                        if proc.is_running():
                            proc.kill()
                    except:
                        pass

                    log_alert(
                        "process_monitor",
                        "HIGH",
                        f"Suspicious process {name} detected and terminated"
                    )

            except:
                continue

        time.sleep(0.2)

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from modules.clamav_scanner import scan_file
from modules.logger import log_alert
import time
import os

class FileHandler(FileSystemEventHandler):

    def scan_detected_file(self, file_path):
        print("[INFO] Scanning:", file_path)

        infected, output = scan_file(file_path)

        if infected:
            print("[ALERT] Malware detected!")

            # 🔥 DELETE MALWARE FILE
            try:
                os.remove(file_path)
                print("[ACTION] Malware file deleted!")
                
                log_alert(
                    "file_scan",
                    "HIGH",
                    f"Malware detected and deleted: {file_path}"
                )
            except Exception as e:
                print("[ERROR] Could not delete file:", e)

        else:
            # ❌ Optional: remove this if you want cleaner output
            print("[INFO] File is clean")
            log_alert("file_scan", "LOW", f"File scanned clean: {file_path}")

    def on_created(self, event):
        if not event.is_directory:
            print("[INFO] New file detected:", event.src_path)
            self.scan_detected_file(event.src_path)


def start_monitoring(path):

    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    observer.start()

    print("[INFO] Monitoring folder:", path)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

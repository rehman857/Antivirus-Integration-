from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from modules.clamav_scanner import scan_file
from modules.logger import log_alert
import time

class FileHandler(FileSystemEventHandler):

    def scan_detected_file(self, file_path):
        print("[INFO] Scanning:", file_path)

        infected, output = scan_file(file_path)

        if infected:
            print("[ALERT] Malware detected!")
            log_alert("file_scan", "HIGH", f"Malware detected in {file_path}")
        else:
            print("[INFO] File is clean")
            log_alert("file_scan", "LOW", f"File scanned clean: {file_path}")

    def on_created(self, event):
        print("DEBUG EVENT:", event.src_path)

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

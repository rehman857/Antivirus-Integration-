from modules.clamav_scanner import scan_file
from modules.logger import log_alert

if __name__ == "__main__":
    file_path = input("Enter file path to scan: ")

    infected, output = scan_file(file_path)

    if infected:
        print("[ALERT] Malware detected!")
        log_alert("file_scan", "HIGH", "Malware detected in " + file_path)
    else:
        print("[INFO] File is clean.")
        log_alert("file_scan", "LOW", "File scanned clean: " + file_path)

    print(output)

from modules.file_monitor import start_monitoring
from modules.process_monitor import monitor_processes
import threading

if __name__ == "__main__":
    folder = input("Enter folder path to monitor: ")

    t1 = threading.Thread(target=start_monitoring, args=(folder,))
    t2 = threading.Thread(target=monitor_processes)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

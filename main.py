from modules.process_monitor import monitor_processes
from modules.file_monitor import start_monitoring
import threading

t1 = threading.Thread(target=monitor_processes)
t2 = threading.Thread(target=start_monitoring, args=("/home/kali/test_monitor",))

t1.start()
t2.start()

t1.join()
t2.join()


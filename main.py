from modules.file_monitor import start_monitoring

if __name__ == "__main__":
    folder = input("Enter folder path to monitor: ")
    start_monitoring(folder)

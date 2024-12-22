import time
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            log_data = {
                'event_type': event.event_type,
                'src_path': event.src_path,
            }
            with open('/home/ubuntu/bsm/logs/changes.json', 'a') as log_file:
                log_file.write(json.dumps(log_data) + '\n')

if __name__ == "__main__":
    path = "/home/ubuntu/bsm/test"  
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


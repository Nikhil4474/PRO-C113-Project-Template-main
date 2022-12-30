import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = r"C:\Users\Nikhil\Downloads\PRO-C113-Project-Template-main\Class 113 Example"

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):

    #1_on_created
    def on_create(self, event):
        print({event.src.path}, "Has been created")

    #2_on_deleted
    def on_delete(self, event):
        print({event.src.path}, "Has been deleted")

    #3_on_modified
    def on_modified(self, event):
        print({event.src.path}, "Has been modified")

    #4_on_moved
    def on_moved(self, event):
        print({event.src.path}, "Has been moved")
        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt
try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("KeyboardInterrupt")
    observer.stop()

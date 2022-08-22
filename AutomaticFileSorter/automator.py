# Step 0: Detect change in the Download folder
# Step 1: List all files in the Download folder
# Step 2: Categorize the file types based on their extension (.mp3, .mp4,...)
# Step 3: Move each file to its destined directory
# Step 4: Check if there is name duplicates

# We will need:
# - Something to detect changes in the folder: watchdog provides Watcher and Handler
# - Something to list all files in the Download folder: os.scandir()
# - Something to move the files: shutil.move()

from importlib.machinery import SourcelessFileLoader
from multiprocessing.reduction import duplicate
import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    DIRECTORY_TO_WATCH = "C:/Users/An/Downloads"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print ("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    def duplicate_check(self, file, folder_files):
        name = file.split('.')[0]
        extension = file.split('.')[1]
        if file in folder_files:
            for index in range(100):
                new_file = f"{name}({index}).{extension}"
                if new_file in folder_files:
                    continue
                break

        return new_file

    def move_file(self, file, source, destination):
        files = os.listdir(destination)
        file = self.duplicate_check(file, files)
        destination = destination + "/" + file

        shutil.move(source, destination)

    def categorize_files(self, source, file_name, extension):
        # Documents
        if extension in ['doc', 'docx', 'pdf', 'txt', 'ppt', 'pptx']:
            destination = "C:/Users/An/Desktop/DownloadedDocuments"
            file = f"{file_name}.{extension}"
            self.move_file(file, source, destination)
            return True

        # Audio
        if extension in ['mp3', 'wav']:
            destination = "C:/Users/An/Desktop/DownloadedAudio"
            file = f"{file_name}.{extension}"
            self.move_file(file, source, destination)
            return True

        # Videos
        if extension in ['mp4', 'mov']:
            destination = "C:/Users/An/Desktop/DownloadedVideos"
            file = f"{file_name}.{extension}"
            self.move_file(file, source, destination)
            return True

        # Images
        if extension in ['png', 'jpg', 'jpeg', 'heic']:
            destination = "C:/Users/An/Desktop/DownloadedImages"
            file = f"{file_name}.{extension}"
            self.move_file(file, source, destination)
            return True

        return False

    def file_sorter(self):
        path = "C:/Users/An/Downloads"
        obj = os.scandir(path)

        for entry in obj :
            if entry.is_file():
                source = path + "/" + entry.name
                file_name = entry.name.split('.')[0]
                extension = entry.name.split('.')[-1]
                self.categorize_files(source, file_name, extension)

    # This is a built-in function name *do not change the name*
    def on_any_event(self, event):
        self.file_sorter()
        

if __name__ == '__main__':
    w = Watcher()
    w.run()


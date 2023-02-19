import os
import datetime
import shutil
 
startingPath = r"***Add your path here***"
date = datetime.date.today()
currentYear = date.year
previousYear = str(currentYear - 1)
 
for root, dirs, files in os.walk(startingPath):
    path = root.split("\\")
    if previousYear in path:
        try:
# Get the last year path
            oldPath = "\\".join(path)
# Get the current year path
            del path[-1]
            path.append(str(currentYear))
            newPath = path
            newPath = "\\".join(newPath)
            shutil.copytree(oldPath, newPath)
            print(f"Folder with this path -> {oldPath} <- copied and renamed -> {currentYear} <-")  
        except FileExistsError:
            print(f"Folder with this path -> {newPath} <- already exists")
#!/usr/bin/python3
import os, os.path
from Folder import Folder

class Folders(list):
    def __init__(self, dir):
        dirs_and_files = os.listdir(dir) 
        for dir_or_file in dirs_and_files:
            path = os.path.join(dir, dir_or_file)
            try: 
                #print(path)
                folder = Folder(path)
                self.append(folder)
            except FileNotFoundError as e: 
                pass

    def saveAll(self):
        for folder in self:
            folder.saveNewPng()

if __name__ == "__main__":
    folders = Folders(".")
    #print(len(folders))
    folders.saveAll()


#!/usr/bin/python3
import os.path, json, Driver
import datetime
import shutil

class Conf(dict):
    def __init__(self, dir):
        if not os.path.isdir(dir):
            raise FileNotFoundError("Expecting to a path to a directory. " + dir)
        self.dir = dir
        self.path = os.path.join(dir, "conf.json")
        self.update(json.load(open(self.path)))
        if "css_selector" not in self:
            self["css_selector"] = "body"

class Last(dict):
    def __init__(self, dir):
        if not os.path.isdir(dir):
            raise RuntimeError("Expecting to a path to a directory. " + dir)
        self.dir = dir
        self.path = os.path.join(dir, "last.json")
        try:#
            self.update(json.load(open(self.path)))
        except json.decoder.JSONDecodeError as e: 
            pass
        except FileNotFoundError as e: 
            pass
        if "datetime" not in self:
            self["datetime"] = "2000-01-01T00:00:00"
        if "interval_seconds" not in self:
            self["interval_seconds"] = 1800

    def datetime(self):
        return datetime.datetime.fromisoformat(self["datetime"])

    def isStale(self):
        now = datetime.datetime.now()
        elapsed = now - self.datetime()
        return elapsed > datetime.timedelta(seconds = self["interval_seconds"])

    def save(self):
        with open(self.path, "wb") as file:
            file.write(json.dumps(self).encode("utf8"))

class Folder():
    def __init__(self, path_to_dir):
        self.path_to_dir = path_to_dir
        self.conf = Conf(path_to_dir)
        self.last = Last(path_to_dir)

    def saveNewPng(self):
        now = datetime.datetime.now()
        now_iso_format = now.isoformat(timespec="seconds")
        new_png_file_name = now_iso_format + "Z.png"
        path = os.path.join(self.path_to_dir, new_png_file_name)
        driver = Driver.Driver()
        driver.savePng(self.conf["url"], self.conf["css_selector"], path)
        del(driver)
        self.last["datetime"] = now_iso_format
        self.last["png_file_name"] = new_png_file_name
        self.last.save()
        shutil.copy(path, os.path.join(self.path_to_dir, "last.png"))


if __name__ == "__main__":
    conf = Conf("test")
    last = Last("test")
    folder = Folder("test")
    print(folder.last.isStale())
    folder.saveNewPng()


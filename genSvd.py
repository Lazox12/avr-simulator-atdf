from os import listdir, getcwd
from os.path import isfile, join
import threading
import sys
import os
import subprocess

def run(path):
    name = path.split("/")[-1].split(".")[0]
    print("generating:",name)
    print(subprocess.run(["cargo","run","--manifest-path","atdf2svd/Cargo.toml","--",path,"svd/"+name],capture_output=True).stdout)

def getAtdf(path)-> list[str]:
    return [join(getcwd(),path,f) for f in listdir(path) if isfile(join(path,f))]

def clean():
    os.remove("svd")

if __name__ == "__main__":
    if len(sys.argv)>2:
        if sys.argv[1] == "clean":
            clean()
            exit(0)
    threads = []
    if not os.path.isdir("svd"):
        os.mkdir("svd")
    for i in getAtdf("avr-registers/atdf"):
        threads.append(threading.Thread(target=run, args=(i,)))
        i.start()

    for i in threads:
        i.join()
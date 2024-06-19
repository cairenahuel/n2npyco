import shutil
import os

from typing import List

def getFilename(path):
    return os.path.basename(path)

def isFileInDir(file: str, dir: str)->bool:
    fileNames = os.listdir(dir)
    return file in fileNames

def existsFiles(copyFrom: List[str])->bool:
    for file in copyFrom:
        if (not os.path.isfile(file)):
            return False
    return True

def existsDirs(copyTo: List[str])->bool:
    for dir in copyTo:
        if (not os.path.isdir(dir)):
            return False
    return True

def copy(copyFrom: List[str], copyTo: List[str]):
    for _from in copyFrom:
        for _to in copyTo:
            shutil.copy(_from, _to)

def copyAndReplace(copyFrom: List[str], copyTo: List[str]):
    for _from in copyFrom:
        for _to in copyTo:
            if (isFileInDir(_from,_to)):
                fileName = getFilename(_from)
                fileToRemove = os.path.join(_to,fileName)
                os.remove(fileToRemove)
            shutil.copy(_from, _to)
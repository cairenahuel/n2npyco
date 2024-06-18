import shutil
def copy(copyFrom: [str], copyTo: [str]):
    for _from in copyFrom:
        for _to in copyTo:
            shutil.copy(_from, _to)
import os


def write(content: str, fpath: str):
    with open(fpath, "w") as _file:
        _file.write(content)


def read(fpath: str):
    with open(fpath, "r") as _file:
        return _file.read()


def file_size(f_path):
    if os.path.isfile(f_path):
        return int(os.path.getsize(f_path))
    return 0

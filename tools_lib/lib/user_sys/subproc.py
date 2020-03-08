import subprocess
import tempfile


def read(cmd: list, encoding="utf-8"):
    with tempfile.TemporaryFile() as temp_f:
        proc = subprocess.Popen(" ".join(cmd), shell=True, stdout=temp_f)
        proc.wait()
        temp_f.seek(0)
        return temp_f.read().decode(encoding)


def read_sub(cmd: list, encoding="utf-8"):
    with tempfile.TemporaryFile() as temp_f:
        proc = subprocess.Popen(" ".join(cmd), shell=True, stdout=temp_f)
        proc.wait()
        temp_f.seek(0)
        return temp_f.read().decode(encoding)

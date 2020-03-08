import subprocess
from typing import Optional


def sub_com(command, input_pipe=None) -> Optional[str]:
    stderr = ""
    # subprocess communicate
    # https://stackoverflow.com/questions/11269575/how-to-hide-output-of-subprocess-in-python-2-7

    # Command Should be None, guard for False for sanity
    if command is None or command is False:
        return None
    try:
        response = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    shell=True)
        if input_pipe is None or input_pipe is False:
            stdout, stderr = response.communicate()
            stdout = stdout.decode()
            stderr = stderr.decode()
        else:
            stdout, stderr = response.communicate(input=input_pipe.encode())
            stdout = stdout.decode()
            stderr = stderr.decode()
        if stderr != '':
            raise OSError
    except OSError as e:
        print("SUB COM ERROR")

        # stdout = False
        return None
    return stdout

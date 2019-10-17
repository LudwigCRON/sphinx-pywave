#!/usr/bin/env python3

import sys
import shlex
import subprocess

def sh_exec(cmd: str, log: str = None, mode: str = "w+",
            MAX_TIMEOUT: int = 300, SHOW_CMD: bool = False, SHELL: bool = False,
            CWD: str = None):
    """
    simplify code for executing shell command
    """
    try:
        if CWD is None:
            proc = subprocess.Popen(shlex.split(cmd),
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT, shell=SHELL)
        else:
            proc = subprocess.Popen(shlex.split(cmd),
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT, shell=SHELL, cwd=CWD)
        if not log is None:
            with open(log, mode) as fp:
                if SHOW_CMD:
                    fp.write(cmd+'\n')
                for line in proc.stdout:
                    sys.stdout.write(line.decode('utf-8'))
                    fp.write(line+"\n")
        else:
            for line in proc.stdout:
                sys.stdout.write(line.decode('utf-8'))
        proc.stdout.close()
        return_code = proc.wait()
        if return_code:
            raise subprocess.CalledProcessError(return_code, cmd)
    except (OSError, subprocess.CalledProcessError) as exception:
        print("Exception occured: ", str(exception))
        return False
    except subprocess.TimeoutExpired as te:
        print("Unexpected executer timeout")
        return False
    else:
        return True

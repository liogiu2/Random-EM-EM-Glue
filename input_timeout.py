import os
if os.name == 'nt':
    import msvcrt
import time
import sys
import select

class TimeoutExpired(Exception):
    pass

def input_with_timeout(prompt, timeout, timer=time.monotonic):
    if os.name == 'nt':
        sys.stdout.write(prompt)
        sys.stdout.flush()
        endtime = timer() + timeout
        result = []
        while timer() < endtime:
            if msvcrt.kbhit():
                result.append(msvcrt.getwche()) #XXX can it block on multibyte characters?
                if result[-1] == '\r':
                    return ''.join(result[:-1])
            time.sleep(0.04) # just to yield to other processes/threads
        raise TimeoutExpired
    else:
        sys.stdout.write(prompt)
        sys.stdout.flush()
        ready, _, _ = select.select([sys.stdin], [],[], timeout)
        if ready:
            return sys.stdin.readline().rstrip('\n') # expect stdin to be line-buffered
        raise TimeoutExpired
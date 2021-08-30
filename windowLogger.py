from utils import *
from datetime import datetime
from datetime import timedelta

import atexit
#import ctypes
#ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


def exit_handler():
    log_end_to_file(appTimeStart)


atexit.register(exit_handler)

try:
    # initialisation

    #datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    loggingStart = datetime.now().replace(microsecond=0)
    log_start_to_file(loggingStart)

    activeWindow = get_active_exe_name()
    previousWindow = activeWindow

    appTimeStart = datetime.now().replace(microsecond=0)

    isIdle = False
    idleStart = None

    # main code
    while True:
        activeWindow = get_active_exe_name()
        if activeWindow != previousWindow:
            log_app_activity_to_file(previousWindow, appTimeStart)
            appTimeStart = datetime.now().replace(microsecond=0)

        previousWindow = activeWindow

        idleDuration = get_idle_duration()
        if idleDuration > 120:
            if isIdle == False:
                isIdle = True
                idleStart = datetime.now().replace(microsecond=0) - timedelta(minutes=2)
        else:
            if isIdle == True:
                log_idle_to_file(idleStart)
                isIdle = False


finally:
    log_end_to_file(appTimeStart)

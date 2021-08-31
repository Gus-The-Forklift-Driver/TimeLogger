from time import sleep
import win32gui
import win32process
import wmi
from ctypes import Structure, windll, c_uint, sizeof, byref
from datetime import datetime

'''
class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


'''


class color:
    HEADER = ''
    OKBLUE = ''
    OKCYAN = ''
    OKGREEN = ''
    WARNING = ''
    FAIL = ''
    END = ''
    BOLD = ''
    UNDERLINE = ''


def get_active_exe_name():
    procs = wmi.WMI().Win32_Process()

    pycwnd = win32gui.GetForegroundWindow()
    tid, pid = win32process.GetWindowThreadProcessId(pycwnd)

    for proc in procs:
        if proc.ProcessId == pid:
            return proc.Name.replace(".exe", "")
    return "none"


class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]


def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0


def log_start_to_file(start):
    print(f'{color.WARNING}---------------------------{color.END}')
    print(f'{color.OKBLUE}Started logging at {color.OKCYAN}{start}{color.END}')
    with open('active.csv', 'a') as outfile:
        outfile.write(f'\n{start},{start}')


def replace_end_to_file(start):
    end = datetime.now().replace(microsecond=0)
    #duration = end - start
    # print(f'{color.WARNING}---------------------------{color.END}')
    # print(f'{color.OKBLUE}Ended logging {color.OKCYAN}{start}{color.#OKBLUE} ended at {color.OKCYAN}{end}{color.OKBLUE}, for {color.#OKCYAN}{duration}{color.OKBLUE}{color.END}')

    with open('active.csv', 'r') as outfile:
        data = outfile.readlines()
    # remove last line from file
    data = data[:-1]
    data.append(f'{start},{end}')
    with open('active.csv', 'w') as outfile:
        outfile.writelines(data)


def log_app_activity_to_file(app, start):
    end = datetime.now().replace(microsecond=0)
    duration = end - start
    print(f'{color.HEADER}---------------------------{color.END}')
    print(f'{color.OKBLUE}{app} started at {color.OKCYAN}{start}{color.OKBLUE} ended at {color.OKCYAN}{end}{color.OKBLUE}, for {color.OKCYAN}{duration}{color.OKBLUE}{color.END}')
    with open('apps.csv', 'a') as outfile:
        outfile.write(f'\n{app},{start},{end}')


def log_idle_to_file(start):
    end = datetime.now().replace(microsecond=0)
    duration = end - start
    print(f'{color.WARNING }---------------------------{color.END}')
    print(f'{color.OKGREEN }Idle from {color.OKCYAN}{start}{color.OKBLUE} ended at {color.OKCYAN}{end}{color.OKBLUE}, for {color.OKCYAN}{duration}{color.OKBLUE}{color.END}')
    with open('idle.csv', 'a') as outfile:
        outfile.write(f'\n{start},{end}')

# TimeLogger
**This is yet only compatible with Windows only**
This is a simple script that log activity on your computer. It works by reading the active window executable name.


# Setup

You can make it start automatically at login using the Windows task scheduler to run the .bat file. 
If you dont want the terminal you can uncomment these two lines :
'''
import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
'''

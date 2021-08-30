# TimeLogger
**This is yet only compatible with Windows only.**

This is a simple script that log activity on your computer. It works by reading the active window executable name.

# Dependencies

* python 3.8.6

* Modules:
   * squarify (for data viz only)
   * pandas (for data viz only)


Install with ```pip install squarify pandas``` or with ```python -m pip install squarify pandas```.

# Setup

You can make it start automatically at login using the Windows task scheduler to run the .bat file. 
If you dont want the terminal you can uncomment these two lines :
```python
import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
```
You should then start the script with ```python windowLogger.py``` instead of the .bat file in Task Scheduler.

# Visualising the data

To visualise the data use the viewer.py 

_This is a work in progress._

_This only allow to see a sum up of app activity._

# Todo

 - [ ] code cleanup and commenting
 - [ ] cross-platform
 - [ ] create ui to visualize the data
 - [ ] gess active web browser page

# Known Bugs

* When shutting down the computer the logging end doesnt register propely.

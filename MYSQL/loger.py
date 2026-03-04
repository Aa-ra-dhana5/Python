#basicConfig(**kwargs)  method is used to config logging system --it appends the data
# filename, filemode, level, formate, datefmt, style, stream ,handler , force

# LEVELS
'''
NOTSET   0
DEBUG    10
INFO     20
WARNING  30 -- default
ERROR    40
CRITICAL 50
'''

#Methods
'''
1. getLogger()  -- return root if name not provided
2. info(msg) -- level INFO on this logger
3. warninng(msg) --ERROR level
'''

# Formate -- can take a string with LogRecord attributes in any arrangement you like 
# asctime - Human readable time when the LofRecord was created.


# mylib.py
from logging import *


Log_formate = '%(asctime)s --%(message)s'
Log_formate2 = '{name} -- {asctime} --{message}'


basicConfig(filename='logfile.log', level=DEBUG, filemode='w', style='{' , format=Log_formate2)

loggerName = getLogger('max')
debug("this is debug with write mode")
loggerName.warning("this is warning")
error("this is error")
critical("this is critical")
# all for windows

import psutil
import sys
import os
import platform

services_list = list(psutil.win_service_iter())

# print the services
#[print(service) for service in services_list]

# print PID, NAME, and STATUS of all services
def printStatus(s):
    print(s.pid(), s.name(), psutil.win_service_get(s.name()).status())
    

[printStatus(service) for service in services_list]

print(sys.platform)
print(os.name)
print(platform.platform())

# This script pings the list of IP addresses and shows the result in a
# designated output file.

import os
import sys
import subprocess


ping_hosts = open('pinghosts.txt','r')
for ip in ping_hosts:
    file = open('pingresults.txt','a')
    ip = ip.strip()
    response = str(subprocess.check_output(['ping', ip]))
    response = response.split('\\r\\n')
    for x in response:
        x = x.strip()
        x = x.strip("'")
        if x == 'b':
            x = 'Ping to ' + ip
        file.write(x)
        file.write('\n')
    file.close()

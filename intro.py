import os
import sys

import requests

print(sys.version)
print(sys.executable)


print(os.getcwd())

print(os.__file__)

try:
    r = requests.get('https://www.google.com')
    print(r.status_code)
    print(r.ok)
except:
    print('Could not open url')

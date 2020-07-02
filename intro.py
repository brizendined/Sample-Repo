import os
import sys

import requests

print(sys.version)
print(sys.executable)


print(os.getcwd())

print(os.__file__)

r = requests.get('www.google.com')
print(r.status_code)
print(r.ok)

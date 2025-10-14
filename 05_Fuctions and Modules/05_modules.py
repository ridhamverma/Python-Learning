# # Two types of modules in Python:
# Build in Modules
# External Modules
# List of all the built in modules : https://docs.python.org/3/py-modindex.html
import math
import os
import mymodule
import requests

print(math.sqrt(16))
mymodule.hello()
r = requests.get("https://www.google.com")
print(r.text)

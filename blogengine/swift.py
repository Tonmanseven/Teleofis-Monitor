import os
import sys
import time
import json
from urllib import request


response = request.urlopen("http://localhost:8000/swift.html?hostname=mark_014&start=05/03/2019$-$05/04/2019")

print(response)




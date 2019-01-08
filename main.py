#!/usr/bin/env python
import requests
print(requests.__version__)
test = requests.get("http://www.google.com/")
print(test)

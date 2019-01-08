#!/usr/bin/env python
import requests
print(requests.__version__)
test = requests.get("http://www.google.com/")
raw = requests.get(
    "https://raw.githubusercontent.com/pennyfea/cmut404-lab1/master/main.py")
# print(dir(test))
print(raw.text)

#!/usr/bin/python3
import pandas as pd
import re


rex = r'(?P<TIME>[A-Z][a-z]{2} [ \d]\d \d\d:\d\d:\d\d) (?P<HOSTNAME>.+?)\s(?P<DAEMON>.+?): (?P<MESSAGE>.+$)'
r = re.compile(rex)

extracted = []
with open('super_auth.log', 'r') as f:
    for line in f.readlines():
        extracted.append(r.search(line).groups())

df = pd.DataFrame(extracted, columns=['time', 'host', 'logger', 'message'])

print(df.info())

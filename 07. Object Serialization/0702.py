# JSON - Javascritp Object Notation
# An extremely popular standard for storing
# communicating structured data
# It is Human readable
# often used for configuration files
# this is not a valid python

import json

# load the content of the json file
with open("sample.json") as fp:
    details = json.load(fp)
    print(details)


# write to the json file
# first we have to load the content file
with open("sample.json", 'w') as fp:
    details['hobby'] = "Poetry"
    json.dump(details, fp)


# load the content of the json file
with open("sample.json") as fp:
    details = json.load(fp)
    print(details)

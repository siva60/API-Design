#  utils file helps to check data that's coming through is a valid json


import json


# this method just returns a boolean value
def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid



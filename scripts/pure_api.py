import requests
import json
BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/"


def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    data = r.json()

    for item in data:
        if item['id'] == 1:
            r2 = requests.get(BASE_URL + ENDPOINT + str(item['id']))
            # print(r2.json())

    return data


def create_update():
    new_data = {
        'user': 1,
        'content': "Another user siva Update"
    }
    r = requests.post(BASE_URL + ENDPOINT + "1/", data=new_data)
    # print(r.status_code)
    # print(r.headers)
    if r.status_code in range(200, 299):
        return r.json()
    return r.text


def do_obj_update():
    new_data = {
        'content': "This is updated user Update using put method"
    }
    r = requests.put(BASE_URL + ENDPOINT + "1/", data=json.dumps(new_data))
    print(r.status_code)
    if r.status_code in range(200, 299):
        return r.json()
    return r.text


print(get_list())
# print(create_update())

# print(do_obj_update())


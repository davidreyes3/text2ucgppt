import json


def convert_json_to_hymn_slide_dict(json_data):
    dictt = json.loads(json_data)

    for d in dictt.values:
        print(d)


HYMN_SLIDE_JSON_PATH = '../resources/hymn_slide.json'
with open(HYMN_SLIDE_JSON_PATH) as json_file:
    hymn_slide_json = json.load(json_file)

    for d in hymn_slide_json:
        print(d)

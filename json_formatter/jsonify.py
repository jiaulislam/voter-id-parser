import json


def make_json_file(parsed_data) -> None:
    """
    Make a file in Json formatted object
    """
    with open("parsed_data.json", "w", encoding='utf-8') as json_file:
        json.dump(parsed_data, json_file, ensure_ascii=False, indent=4)


def export_json(data: dict) -> str:
    """
    Output the Json formatted object
    """
    return json.dumps(data, indent=4, ensure_ascii=False)

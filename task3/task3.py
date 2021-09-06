"""
На вход в качестве аргументов программы поступают два файла: tests.json и values.json (в приложении к заданию находятся
примеры этих файлов)
• values.json содержит результаты прохождения тестов с уникальными id
• tests.json содержит структуру для построения отчёта на основе прошедших тестов
(вложенность может быть большей, чем в примере)
Напишите программу, которая формирует файл report.json с заполненными полями value для структуры tests.json на
основании values.json.
Пример:
Часть структуры tests.json:
{"id": 122, "title": "Security test", "value": "", "values":
[{"id": 5321, "title": "Confidentiality", "value": ""},
{"id": 5322, "title": "Integrity", "value": ""}]}

После заполнения в соответствии с values.json:
{"values": [{"id": 122, "value": "failed"}, {"id": 5321,"value": "passed"}, {"id": 5322,"value": "failed"}]}

Будет иметь следующий вид в файле report.json:
{"id": 122, "title": "Security test", "value": "failed", "values":
[{"id": 5321, "title": "Confidentiality", "value": "passed"},
{"id": 5322, "title": "Integrity", "value": "failed"}]}
"""
import sys
import json



tests_json = sys.argv[1]
values_json = sys.argv[2]
report = "report.json"

values_dict = {}

with open(f"{values_json}", "r") as read_file:
    values_json = json.load(read_file)

values_array = (values_json['values'])

for item in values_array:  # Make values_dict, key - it's "id" from values_json, "value" - value
    key = item.get('id')
    value = item.get('value')
    values_dict.update({key: value})

with open(f"{tests_json}", "r") as read_file:
    tests_json = json.load(read_file)

test_array = (tests_json['tests'])


def change_value_in_string(string):
    """
    This function append value for id from values_json to test_array.
    If we get inserted dict "values", function open it as "string"  call themself and continue iteration.

    :param string: element of list test_array
    :return: values_dict, string
    """
    global values_dict
    for element in string:
        if element["id"] in values_dict:
            element["value"] = values_dict.get(element["id"])
        else:
            pass
        if "values" in element:
            if element["id"] in values_dict:
                element["value"] = values_dict.get(element["id"])
            else:
                pass
            string = element["values"]
            change_value_in_string(string)
    return values_dict, string


for elem in test_array:
    i = elem["id"]
    elem['value'] = values_dict.get(i)
    if "values" in elem:
        string = elem["values"]
        change_value_in_string(string)

with open(f"{report}", "w", encoding="utf-8") as file:
    json.dump(test_array, file, ensure_ascii=False)






import json

# dumps: convert a Python object to a JSON string
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
print('type of data is dict: ', type(data))
json_data = json.dumps(data)
print('after dumps: ', json_data)
print('after dumps: ', type(json_data))

# loads: convert a JSON string back to a Python object
json_data = json.loads(json_data)
print('after load', json_data)
print('after load', type(json_data))

# dump: write a Python object to a file in JSON format
with open('data.json', 'w') as f:
    json.dump(data, f)

# load: read a JSON file and convert it back to a Python object
with open('data.json', 'r') as f:
    data_from_file = json.load(f)
print('data from file: ', data_from_file)

# ensure_ascii
data_from_file['city'] = '北京'
data_from_file_json = json.dumps(data_from_file)
print('data from file in different language: ', data_from_file_json)    # Chinese converted to Unicode
data_from_file_json = json.dumps(data_from_file, ensure_ascii=False)
print('data from file in different language: ', data_from_file_json)
# indent
data_from_file_json = json.dumps(data_from_file, indent=4, ensure_ascii=False)
print('data from file with indent: ', data_from_file_json)
# sort_keys
data_from_file_json = json.dumps(data_from_file, indent=4, ensure_ascii=False, sort_keys=True)
print('data from file with sorted keys: ', data_from_file_json)
# separation
data_from_file_json = json.dumps(data_from_file, indent=4, ensure_ascii=False, separators=(',', '= '))
print('data from file with separators: ', data_from_file_json)


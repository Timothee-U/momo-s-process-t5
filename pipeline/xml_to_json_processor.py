import json
import xmltodict

# Reading from the file
with open('../storage/input/modified_sms_v2.xml', mode="r") as file:
    raw_data = file.read()
    print(type(raw_data))

    sms_dict = xmltodict.parse(raw_data)
    data = json.dumps(sms_dict, indent=4)
    print(data)

import json

#with open('JSON/r1.json') as file:
    #data = json.load(file)
    #json.load is for loading and interpreting a file
    #loads a file

#router_json = '''
#{
#    "router": {
#        "hostname": "R1",
#        "interfaces": [
#            {
#                "id": "0",
#                "enabled": "true",
#                "name": "GigabitEthernet0/0",
#                "ip": "192.168.1.254",
#                "mask": "255.255.255.0"
#            },
#            {
#                "id": "1",
#                "enabled": "true",
#                "name": "GigabitEthernet0/1",
#                "ip": "172.16.1.2",
#                "mask": "255.255.255.0"
#            }
#        ],
#        "routing": {
#            "routes": [
#                {
#                    "destination": "192.168.2.0",
#                    "mask": "255.255.255.0",
#                    "gateway": "192.168.1.253"
#                },
#                {
#                    "destination": "0.0.0.0",
#                    "mask": "0.0.0.0",
#                    "gateway": "201.1.113.54"
#                }
#            ]
#        }
#    }
#}
#'''

#data = json.loads(router_json)
    #json.loads is for when we've already got the string of JSON in RAM and need to convert to python dictionary
    #loads a string

#print(data['router']['interfaces'][0])

router_dict = {
    "router": {
        "hostname": "R1",
        "interfaces": [
            {
                "id": "0",
                "enabled": "true",
                "name": "GigabitEthernet0/0",
                "ip": "192.168.1.254",
                "mask": "255.255.255.0"
            },
            {
                "id": "1",
                "enabled": "true",
                "name": "GigabitEthernet0/1",
                "ip": "172.16.1.2",
                "mask": "255.255.255.0"
            }
        ],
        "routing": {
            "routes": [
                {
                    "destination": "192.168.2.0",
                    "mask": "255.255.255.0",
                    "gateway": "192.168.1.253"
                },
                {
                    "destination": "0.0.0.0",
                    "mask": "0.0.0.0",
                    "gateway": "201.1.113.54"
                }
            ]
        }
    }
}

router_json = json.dumps(router_dict)
print(router_json)

with open('JSON/data.json', 'w') as file:
    json.dump(router_dict, file, indent=2)
    #opens a new file (data.json) and dump router_dict into the file

#load = import a file
#loads = json in RAM
#dump = export to file
#dumps = hold the new JSON in RAM
#if ends in s, hold in RAM, if not, input from/output to file

#load and loads
    #json to dictionary
#dump and dumps
    #dictionary to json
#load vs loads
    #import from file vs import from RAM (string)
#dump vs dumps
    #export to file vs converting in RAM
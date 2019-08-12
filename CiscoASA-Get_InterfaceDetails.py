import requests
import json
from pprint import pprint
import ssl

#This pulls the data from the Cisco ASA API under the PHYSICAL path

ssl._create_default_https_context == ssl._create_unverified_context
headers = {'Content-Type': 'application/json'}
def request ():
    r = requests.get(" https://192.168.150.210/api/interfaces/physical", auth=('admin', 'admin'), verify=False, headers=headers)

#This loads the json data from the text output of the RESTAPI

    json_obj = json.loads(r.text)

#this creates a variable in the ITEMS schema

    json_items = json_obj["items"]

#This prints the entire JSON schema

#    print(json.dumps(json_items, indent=4, sort_keys=True))

#this will attempt to print out the interface hardware ID and IP address, if there is no IP address assigned it will fail because the return value is a string instead of a dictionary

    try:
        for i in json_items:
            print("Hardware ID: ",i["hardwareID"])
            print("Interface name: ",i["name"])
            print("IP address: ",i["ipAddress"]["ip"]["value"])
            print("Subnet Mask: ",i["ipAddress"]["netMask"]["value"])
            print("")

    except TypeError:
        print("This interface has no IP address assigned")




if __name__ == '__main__':
    request()  

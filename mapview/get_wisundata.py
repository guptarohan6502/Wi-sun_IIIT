import requests
import json
import re
import time
with open("assets\data.csv", "r") as datafile:
    resp = datafile.readlines()[-1]
print(resp)
new_resp1 = resp

def get_data(uri, data_format="json"):
    """
    Method description:
    Deletes/Unregisters an application entity(AE) from the OneM2M framework/tree
    under the specified CSE
    Parameters:
    uri_cse : [str] URI of parent CSE
    ae_name : [str] name of the AE
    fmt_ex : [str] payload format
    """
    headers = {
        'X-M2M-Origin': 'devtest:devtest',
        'Content-type': 'application/{}'.format(data_format)}

    response = requests.get(uri, headers=headers)
    #print('Return code : {}'.format(response.status_code))
    #print('Return Content : {}'.format(response.text))
    new_resp = json.loads(response.text)["m2m:cin"]["con"]
    time = json.loads(response.text)["m2m:cin"]["ct"]

    # if(resp != new_resp):
    # 	print(new_resp)
    # 	resp = new_resp

    return new_resp,time
    #     try:
    #         for _resp in re.findall("_to_"):
    #             print(_resp)
    #     except:
    #
    #
    #          print("vaibhv")

start = 84900
while True:
    new_resp,time1 = get_data("http://dev-onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WiSUN/Ack/la")
    fin_time = int(time1[9:11])*60*60+int(time1[11:13])*60+int(time1[13:15]) - start
    if("_to_" in new_resp):
        new_resp1 = new_resp.replace("_to_", ",")+","+str(fin_time)+"\n"

    if(resp != new_resp1):
        data_file = open("assets\data.csv", "a")
        data_file.write(new_resp1)
        print(type(time1))
        print(new_resp1)
        resp = new_resp1
        data_file.close()

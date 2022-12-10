import json
import requests
import time
import datetime


def create_cin(uri_cnt, value, cin_labels="", data_format="json"):
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
        'Content-type': 'application/{};ty=4'.format(data_format)}

    body = {
        "m2m:cin": {
            "con": "{}".format(value),
            "lbl": cin_labels,
            "cnf": "text"
        }
    }

    try:
        response = requests.post(uri_cnt, json=body, headers=headers)
    except TypeError:
        response = requests.post(
            uri_cnt, data=json.dumps(body), headers=headers)
    print('Return code : {}'.format(response.status_code))
    print('Return Content : {}'.format(response.text))


def chk_poles():
    nodes = [["WN-LP02-02", ".LP02ON", ".LP02OFF", ".LP02STS", ".LP02CHK"], ["WN-LP03-02", ".LP03ON", ".LP03OFF", ".LP02STS", ".LP03CHK"],
             ["WN-LP04-02", ".LP04ON", ".LP04OFF", ".LP04STS",
                 ".LP04CHK"], ["WN-LP05-02", ".LP05ON", ".LP05OFF", ".LP05STS", ".LP05CHK"],
             ["WN-LP01-03", ".LP01ON", ".LP01OFF", ".LP01STS",
                 ".LP01CHK"], ["WN-LP06-01", ".LP06ON", ".LP06OFF", ".LP06STS", ".LP06CHK"],
             ["WN-LP07-01", ".LP07ON", ".LP07OFF", ".LP07STS",
                 ".LP07CHK"], ["WN-LP08-01", ".LP08ON", ".LP08OFF", ".LP08STS", ".LP08CHK"],
             ["WN-LP09-01", ".LP09ON", ".LP09OFF", ".LP09STS",
                 ".LP09CHK"], ["WN-LP10-01", ".LP10ON", ".LP10OFF", ".LP10STS", ".LP10CHK"],
             ["WN-LP11-01", ".LP11ON", ".LP11OFF", ".LP11STS",
                 ".LP11CHK"], ["WN-LP12-01", ".LP12ON", ".LP12OFF", ".LP12STS", ".LP12CHK"],
             ["WN-LP13-01", ".LP13ON", ".LP13OFF", ".LP13STS",
                 ".LP13CHK"], ["WN-LP14-01", ".LP14ON", ".LP14OFF", ".LP14STS", ".LP14CHK"],
             ["WN-LP15-01", ".LP15ON", ".LP15OFF", ".LP15STS",
                 ".LP15CHK"], ["WN-LP16-01", ".LP16ON", ".LP16OFF", ".LP16STS", ".LP16CHK"],
             ["WN-LP17-01", ".LP17ON", ".LP17OFF", ".LP17STS",
                 ".LP17CHK"], ["WN-LP18-01", ".LP18ON", ".LP18OFF", ".LP18STS", ".LP18CHK"],
             ["WN-LP19-01", ".LP19ON", ".LP19OFF", ".LP19STS",
                 ".LP19CHK"], ["WN-LP20-01", ".LP20ON", ".LP20OFF", ".LP20STS", ".LP20CHK"],
             ["WN-LP21-01", ".LP21ON", ".LP21OFF", ".LP21STS",
                 ".LP21CHK"], ["WN-LP22-01", ".LP22ON", ".LP22OFF", ".LP22STS", ".LP22CHK"],
             ["WN-LP23-01", ".LP23ON", ".LP23OFF", ".LP23STS",
                 ".LP23CHK"], ["WN-LP24-01", ".LP24ON", ".LP24OFF", ".LP24STS", ".LP24CHK"],
             ["WN-LP25-01", ".LP25ON", ".LP25OFF", ".LP25STS",
                 ".LP25CHK"], ["WN-LP26-01", ".LP26ON", ".LP26OFF", ".LP26STS", ".LP26CHK"],
             ["WN-LP27-01", ".LP27ON", ".LP27OFF", ".LP27STS",
                 ".LP27CHK"], ["WN-LP28-01", ".LP28ON", ".LP28OFF", ".LP28STS", ".LP28CHK"],
             ["WN-LP29-01", ".LP29ON", ".LP29OFF", ".LP29STS", ".LP29CHK"], ["WN-LP30-01", ".LP30ON", ".LP30OFF", ".LP30STS", ".LP30CHK"], ]

# data= ".LP02
    for x in range(0, len(nodes)):
        chk = nodes[x][4]
        node = nodes[x][0]
        create_cin(
            "http://dev-onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/"+node+"/Status", chk)
        time.sleep(10)


while True:
    file1 = open("assets\data.csv", "w")
    file1.write("From,To\n")
    file1.close()
    chk_poles()
    time.sleep(3600000)


#end= time.time()
# print(end-start)

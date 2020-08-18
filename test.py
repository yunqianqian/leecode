import requests
import json
import re

def zstack_conn():
    url = 'http://10.11.24.80:8080/zstack/api/'
    data = {
        "org.zstack.header.identity.APILogInByAccountMsg": {
            "password": "b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86",
            "session": {},
            "accountName": "admin"
        }
    }
    headers = {
        'Content-Type': 'application/json',
    }
    r = requests.post(url, data=json.dumps(data), headers=headers) 
    if r.status_code == 200:
        print ("zstack conn sucess!")
        session_id = re.findall(r'\\\"uuid\\\":\\\"(\w{32})\\\"', r.text)
    else:
        print ("zstack conn failed")
        session_id = None
    return session_id[0]


def list_image(session_id):
    url = 'http://10.11.24.80:8080/zstack/v1/images'
    data = {
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth' + session_id
    }
    r = requests.get(url, data=json.dumps(data), headers=headers)
    if r.status_code == 200:
        # for item in json.loads(r.text)["inventories"]:
        #     print (item["name"])
        return [item["name"] for item in json.loads(r.text)["inventories"]]
    else:
        print ("search image list failed!")


def create_vm():
    Cookie = "1295584999831109632"
    knowledge = ["networkSecurity", "systemSecurity", "applicationSecurity", "toolUsage"]
    Cookie = "1295584999831109632"
    data = {
            "name": "test11",
            "knowledge": knowledge[0],
            "instanceOfferingUuid": "625d991906764f219661ce0b57268c02",
            "imageUuid": "5cb39f2be3cd590a9fcad272755f75ca",
            "l3NetworkUuid": "cec17e1c21114ca9a26e948d0d20e93d",
            "clusterUuid": "640361665671463aa1194706a76d279d"
        }
    cookie={"login_token": Cookie}
    header={"content-type": "application/json;charset=utf-8"}
    response = requests.post("http://10.11.24.80:9001/venus/virtManager/vm/add.do?name=test12&knowledge=networkSecurity&instanceOfferingUuid=625d991906764f219661ce0b57268c02&imageUuid=5cb39f2be3cd590a9fcad272755f75ca&l3NetworkUuid=cec17e1c21114ca9a26e948d0d20e93d&clusterUuid=640361665671463aa1194706a76d279d", cookies=cookie, headers=header)
    response.encoding = response.apparent_encoding
    re = response.status_code
    print(re)
    print(response.text)
    print(response.content)



if __name__ == "__main__":
    create_vm()
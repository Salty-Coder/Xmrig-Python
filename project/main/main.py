import os
import json


def save():
    c = input("COIN: ")
    y = input("YOUR_WALLET_ADDRESS: ")
    w = input("WORKER_NAME: ")
    data = {"coin": c, "wallet": y, "worker": w}
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("INFORMATION SAVE SUCCESS!.\n")
    return data

def get():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            json_data = json.load(f)
            json_data["coin"]
            json_data["wallet"]
            json_data["worker"]
            print("INFORMATION LOAD SUCCESS!.\n")
            return json_data
    except:
        return save()

information = get()

os.system("xmrig.exe -o rx.unmineable.com:3333 -a rx -k -u %s:%s.%s -p x pause" % (information["coin"], information["wallet"], information["worker"]))

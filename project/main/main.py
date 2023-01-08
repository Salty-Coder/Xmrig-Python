# original by Dev-Nergis please show the original some love

import json
import os
import sys

close()
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def save():
    if is_Admin():
        print("")
    else:
        print("Failed to apply msr mod please restart as administrator")
    c = input("COIN: ")
    y = input("YOUR_WALLET_ADDRESS: ")
    w = input("WORKER_NAME: ")
    print("")
    print("1. CPU")
    print("2. CUDA")
    print("3. OPENCL")
    print("4. CUDA + CPU")
    print("5. CUDA + OPENCL")
    print("6. NO CPU + CUDA + OPENCL")
    print("7. ALL")
    print("")
    b = int(input("BACKENDS: "))
    data = {"coin": c, "wallet": y, "worker": w, "backends": b}
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
            json_data["backends"]
            print("")
            print("INFORMATION LOAD SUCCESS!.")
            print("")
            return json_data
    except:
        return save()

xmrig_path = resource_path("xmrig/xmrig.exe")
information = get()
backend = information["backends"]

def cpu_oly():
   os.system("%s -o rx.unmineable.com:3333 -a rx -k -u %s:%s.%s -p x" % (xmrig_path, information["coin"], information["wallet"], information["worker"]))

def cuda_oly():
   os.system("%s --no-cpu --cuda -o rx.unmineable.com:3333 -a rx -k -u %s:%s.%s -p x" % (xmrig_path, information["coin"], information["wallet"], information["worker"]))

def opencl_oly():
   os.system("%s --no-cpu --opencl -o rx.unmineable.com:3333 -a rx -k -u %s:%s.%s -p x" % (xmrig_path, information["coin"], information["wallet"], information["worker"]))

def cc_oly():
   os.system("%s --cuda -o rx.unmineable.com:3333 -a rx -k -u %s:%s.%s -p x" % (xmrig_path, information["coin"], information["wallet"], information["worker"]))

def co_oly():
   os.system("%s --opencl -o rx.unmineable.com:3333 -a rx -k -u %s:%s.%s -p x" % (xmrig_path, information["coin"], information["wallet"], information["worker"]))

def ncco_oly():
   os.system("%s --no-cpu --opencl --cuda -o rx.unmineable.com:3333 -a rx -k -u %s:%s.%s -p x" % (xmrig_path, information["coin"], information["wallet"], information["worker"]))

def all():
   os.system("%s --opencl --cuda -o rx.unmineable.com:3333 -a rx -k -u %s:%s.%s -p x" % (xmrig_path, information["coin"], information["wallet"], information["worker"]))

def start():
    print("Backend: %s" % backend)
    if backend == 1:
        cpu_oly()
    elif backend == 2:
        cuda_oly()
    elif backend == 3:
        opencl_oly()
    elif backend == 4:
        cc_oly()
    elif backend == 5:
        co_oly()
    elif backend == 6:
        ncco_oly()
    elif backend == 7:
        all()

if __name__ == "__main__":
    start()

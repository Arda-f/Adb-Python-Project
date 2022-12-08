from subprocess import getoutput
from time import sleep

connect = getoutput("adb connect 192.168.1.37")

control_level = ""
control_charge_status = ""


print(connect)

def Accounts():
    wifi = getoutput("adb shell dumpsys account -l")
    wifi_list = wifi.splitlines()
    for value in wifi_list:
        value = value.strip()
        if(value.endswith("}")):
            value = value.split(",")
            value[0] = value[0].replace("=",": ")
            value[0] = value[0].replace("{", "")
            print(value[0])

while True:
    print()
    user_input = input("Kullanıcı Komutu: ")
    user_input = user_input.split(":")
    user_input[0] = user_input[0].lower()
    if(user_input[0] == "accounts"):
        Accounts()
    else:
        print("komut uygulanamadı")
    # devices = getoutput("adb shell dumpsys battery")
    # devices.strip()
    # devices_list = devices.splitlines()
    # for value in devices_list:
    #     value = value.strip()
    #     #========================================================#
    #     if value.startswith("level"):
    #         if value.split(":")[1].strip() != control_level:
    #             print("yeni değer: " + value.split(":")[1].strip() + "%") 
    #             control_level = value.split(":")[1].strip()
    #     #========================================================#
    #     if value.startswith("AC"):
    #         if control_charge_status != value.split(":")[1].strip():
    #             if value.split(":")[1].strip() == "false":
    #                 print("şarja takılı değil")
    #             else:
    #                 print("şarja takılı")
    #         control_charge_status = value.split(":")[1].strip()
    
            


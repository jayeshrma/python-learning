# Nested conditional block
device_status="Active"
temprature=35

if device_status=="Active":
    if temprature >35:
        print("Device is overheating")
    elif temprature < 20:
        if True:
            pass
    else:
        print("Device working fine")
else:
    print("Device is offline")
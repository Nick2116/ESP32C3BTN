import data
import network
import time
import asyncio

first = True
connected = False

data.pwrled.value(0) # off
data.statled.value(0) # off

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
def connect_to_wifi():
    global wlan
    global connected
    global first
    if first == True:
        wlan.disconnect()
        first = False
    print(wlan.ifconfig())
    if wlan.ifconfig()[0] != "0.0.0.0" and wlan.isconnected() == True and first != True:
        connected = True
        for b in range(3):
            data.statled.value(1)
            time.sleep(0.6)
            data.statled.value(0)
            time.sleep(0.6)
        return
    data.statled.value(1)
    wlan.scan()
    data.statled.value(0)

    for i in range(10):
        print(f"Connecting... (attempt {i})")
        wlan.disconnect()
        time.sleep(0.25)
        wlan.connect(data.ssid, data.password) # connect to an AP
        time.sleep(3)
        if wlan.isconnected() == True:
            print(connected)
            print(wlan.ifconfig())
            connected = True
            for b in range(3):
                data.statled.value(1)
                time.sleep(0.6)
                data.statled.value(0)
                time.sleep(0.6)
            data.statled.value(0)
            
            break
        else:
            for b in range(3):
                data.statled.value(1)
                time.sleep(0.17)
                data.statled.value(0)
                time.sleep(0.17)
            time.sleep(1)
    print(connected)
    if connected == False:
        print("Gave up!")
        data.statled.value(1)
        while True:
            time.sleep(30)

connect_to_wifi()

#while True:
#    time.sleep(30)
            
            
# ---------------------------------------------------------------------------- #


from microdot import Microdot
from microdot import redirect
from math import floor
import _thread

app = Microdot()
pwr = False

def wlan_check():
    while True:
        if wlan.isconnected() == False:
            print(wlan.isconnected())
            connected = wlan.isconnected()
            connect_to_wifi()
        time.sleep(60)

def power_on():
    global pwr
    print(pwr)
    data.pwrled.on()
    time.sleep(1)
    data.pwrled.off()
    pwr = True
    
def power_off():
    global pwr
    print(pwr)
    data.pwrled.on()
    time.sleep(5)
    data.pwrled.off()
    pwr = False
    
@app.route('/')
async def index(request):
    return data.htm(), {'Content-Type': 'text/html'}

@app.route('/power/on')
async def index(request):
    _thread.start_new_thread(power_on, ())
    return redirect("/")

@app.route('/power/off')
async def index(request):
    _thread.start_new_thread(power_off, ())
    return redirect("/")

@app.route('/ping')
async def index(request):
    data.statled.value(1)
    time.sleep(0.25)
    data.statled.value(0)
    return redirect("/")

_thread.start_new_thread(wlan_check, ())
app.run(port=80)

#v1.2
from machine import Pin
from time import time
from time import ticks_ms
from time import sleep_ms
from math import floor

import _thread
epoch = time()
up = 0
detail = ""

def timer():
    global up
    global detail
    while True:
        up = up+1
        sleep_ms(1)
        detail = f"Firmware: v1.2 | Uptime: {moment(up)}"
        
_thread.start_new_thread(timer, ())

def moment(milliseconds):
    seconds = (milliseconds / 1000) % 60
    seconds = int(seconds)

    minutes = (milliseconds / (1000 * 60)) % 60
    minutes = int(minutes)

    hours = (milliseconds / (1000 * 60 * 60)) % 24
    hours = int(hours)

    days = (milliseconds / (1000 * 60 * 60 * 24))
    days = int(days)

    if days > 0:
        return f"{days}d {hours}h {minutes}m {seconds}s"
    elif hours > 0:
        return f"{hours}h {minutes}m {seconds}s"
    elif minutes > 0:
        return f"{minutes}m {seconds}s"
    else:
        return f"{seconds}s"

ssid = ""
password = ""

with open('wifi.txt') as f:
    arr = f.read().split("\n")
    ssid = arr[0]
    password = arr[1]


pwrled = Pin(8,Pin.OUT)
statled = Pin(9,Pin.OUT)



css = """
<style>
* {color-scheme:dark}
body,html {width:fit-content;height:fit-content;margin:16px;padding:0;}
a { padding:9px 18px; border-radius:6px; background:#89b4fa; color:#181825; text-decoration:none; display:inline-block;font-size:16px }
body {background:#1e1e2e;color:#cdd6f4;}
a:hover {opacity:0.9;}
</style>
"""

def htm():
    return f"""
{css}
<pre>
<b style="font-size:24px;margin-bottom:4px;display:inline-block;">ESP Power Button</b>
<a href="/ping">Ping</a> | <a href="/power/on">Short Press</a> | <a href="/power/off">Long Press</a>
<br><br>
<span>{detail}</span>
</pre>
"""

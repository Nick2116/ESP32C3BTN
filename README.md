# ESP32C3 Power Button
An ESP32C3 powered WiFi enabled power button


I had made this because I wanted to be able to turn on my server without actually being there to press a button.
Bought a chinese ESP3C3 super mini and flashed it with LOLIN C3 MINI Micropython Firmware, it works most of the time


Schematic
=============

It is advised to use a larger diode (instead of the signal diode speced).
You dont need to use the same LED as in the image. If you use a Red or Green LED, lower R1 to 500 ohms.

Any NPN BJT should be fine, I used a BC547, but if you have a transistor with less Hfe, lower R2 to fit, as a precaution.

C1 was chosen to help with the stability of the 3v3 line on the ESP32 (you do not need to spec it as large, it was just what I used), as it has a known issue of "browning out" because the linear regulator and onboard filtering cant make up for the surge needed to connect to WiFI.


![schem](https://github.com/user-attachments/assets/d9d37079-5a83-46af-bcd6-d287a2266442)


If you ARE using the same board
===============================
You may use the attatched .bin image

Linux instructions:

git clone this repo into the working directory

run

`esptool.py --chip esp32c3 --port /dev/ttyACM0 erase_flash`

and

`esptool.py --port /dev/ttyACM0  write_flash 0x0000 v1.2.bin`

Access the board from Thonny or your favorite IDE

IN WIFI.TXT, ADD YOUR WIFI CREDENTIALS

Press F5 on main.py and wait for it to connect, watch the serial monitor at the bottom of the screen for its DHCP-Assigned IP

  If you cannot access it from the same network, reboot the ESP32
  
You are good to go!


If you are NOT using the same board 
====================================


Download the attatched files

Copy them into the ESP32 via Thonny or your favorite IDE

IN WIFI.TXT, ADD YOUR WIFI CREDENTIALS

Press F5 on main.py and wait for it to connect, watch the serial monitor at the bottom of the screen for its DHCP-Assigned IP

  If you cannot access it from the same network, reboot the ESP32
  
You are good to go!

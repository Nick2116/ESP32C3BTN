# ESP32C3 Power Button
An ESP32C3 powered WiFi enabled power button

I had made this because I wanted to be able to turn on my server without actually being there to press the power button.
I bought a chinese ESP32C3 super mini and flashed it with LOLIN C3 MINI Micropython Firmware, it works most of the time 🥲.


Schematic
=========

It is advised to use a larger diode (instead of the signal diode speced).
You dont need to use the same LED shown in the schematic, any led with 16mA or less If is fine, ensure Vf is less than 3.3V, and adjust the resistor accordingly.

Any NPN BJT should be fine, I used a BC547, but if you use a transistor with less Hfe (*aka beta or gain*), lower R2 to fit, to ensure proper saturation.
*Valid substitutes would be a 2N2222A, or BC547CBU.*

C1 was chosen to help with the stability of the 3v3 line on the ESP32 (you do not need to spec it as large.), as it has a known issue of "browning out" because the linear regulator and onboard filtering cant make up for the surge needed to connect to WiFI.
*You may add another 220uF capacitor to the 5V rail if you are using a linear regulator or are far away from the power source.*


![schem](https://github.com/user-attachments/assets/5748f1a6-c608-4a47-901a-20ce588e5fe2)



If you ARE using the same board
===============================
You may use the attatched .bin image.

Linux instructions:

git clone this repo into the working directory:

`git clone https://github.com/Nick2116/ESP32C3BTN && cd ESP32C3BTN` *Clones & changes into cloned directory.*

run

`esptool.py --chip esp32c3 --port /dev/ttyACM0 erase_flash` *Cleans flash.*

and

`esptool.py --port /dev/ttyACM0  write_flash 0x0000 v1.2.bin` *Flashes Firmware.*

*Once finished, you may delete the files. `cd .. && rm -r /ESP32C3BTN`*

Access the board from Thonny or your favorite IDE

IN WIFI.TXT, ADD YOUR WIFI CREDENTIALS

Press F5 on main.py and wait for it to connect, watch the serial monitor at the bottom of the screen for its DHCP-Assigned IP, or you can look at the admin panel of your router


  If you cannot access it from the same network, reboot the ESP32
  
You are good to go!


If you are NOT using the same board 
===================================


Download the attatched files

Copy them into the ESP32 via Thonny or your favorite IDE

IN WIFI.TXT, ADD YOUR WIFI CREDENTIALS

Press F5 on main.py and wait for it to connect, watch the serial monitor at the bottom of the screen for its DHCP-Assigned IP, or you can look at the admin panel of your router

  If you cannot access it from the same network, reboot the ESP32
  
You are good to go!


Made with heavy collaboration from [rare1k](https://github.com/uhidontkno) 






# My personal implementation of the system

[image.png](https://github.com/user-attachments/assets/5aacc56a-cf30-47df-ad13-6ffab5559cf7)

It is what is in the schematic but condensed into someting as small as I can make it... Certianly isnt clean though!
